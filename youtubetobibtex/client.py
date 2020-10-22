# youtubetobibtex - Export bibtex from youtube videos
# Copyright (C) 2020 Yoann Piétri

# youtubetobibtex is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# youtubetobibtex is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with youtubetobibtex. If not, see <https://www.gnu.org/licenses/>.

import datetime
import os
import re

import googleapiclient.discovery
import googleapiclient.errors

from youtubetobibtex.errors import (ChannelNotFound, UrlNotSupported,
                                    VideoNotFound)


class YoutubetobibtexClient:
    """
    Main class for interacting with YouTube's api.
    """

    def __init__(self, apikey):

        self.scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        self.api_service_name = "youtube"
        self.api_version = "v3"
        try:
            self.youtube = googleapiclient.discovery.build(
                self.api_service_name, self.api_version, developerKey=apikey
            )
        except googleapiclient.errors.HttpError as e:
            self.youtube = None

        self.TEMPLATE = """
@online{{{citation_name},
    title = {{{title}}},
    date = {{{date}}},
    organization = {{YouTube}},
    author = {{{author}}},
    url = {{{url}}},
}}
        """

    def check(self):
        """Check if the client is valid.

        Returns:
            bool: True if the client is valid, False otherwise.
        """
        return bool(self.youtube)

    def _get_video_info(self, video_id):
        """Get information form the id.

        Args:
            video_id (string): id of the video

        Raises:
            VideoNotFound: if the video wit the given id does not exist
            ChannelNotFound: if no channel is associated with the id with got from the API

        Returns:
            (string, string, datetime): title, author and date of the video.
        """
        request = self.youtube.videos().list(part="snippet", id=video_id)
        videos = request.execute()

        if not videos["items"]:
            raise VideoNotFound("Video {} was not found".format(video_id))

        video = videos["items"][0]
        snippet = video["snippet"]

        request_channels = self.youtube.channels().list(
            part="snippet", id=snippet["channelId"]
        )
        channels = request_channels.execute()

        if not channels["items"]:
            raise ChannelNotFound(
                "Channell {} was not found".format(snippet["channelId"])
            )

        title = snippet["title"]
        author = channels["items"][0]["snippet"]["title"]
        date = datetime.datetime.strptime(snippet["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
        return title, author, date

    def get_bibtex(self, video_id):
        """Get the bibtex entry form the video_id

        Args:
            video_id (string): id of the video

        Returns:
            string: bibtex entry
        """
        title, author, date = self._get_video_info(video_id)
        return self.TEMPLATE.format(
            citation_name="video:{}{}".format(
                author.replace(" ", "").lower(), date.year
            ),
            title=title,
            date=date.year,
            author=author,
            url="https://youtube.com/watch?v={}".format(video_id),
        )

    def get_video_id(self, url):
        """Return the video id from url.

        Several URL schemes are supported.

        Args:
            url (string): url of the video

        Raises:
            UrlNotSupported: if the id cannot be extracted from the url

        Returns:
            string: id of the video
        """
        regexp = re.compile(
            "(?:http:|https:)*?\/\/(?:www\.|)(?:youtube\.com|m\.youtube\.com|youtu\.|youtube-nocookie\.com).*(?:v=|v%3D|v\/|(?:a|p)\/(?:a|u)\/\d.*\/|watch\?|vi(?:=|\/)|\/embed\/|oembed\?|be\/|e\/)([^&?%#\/\n]*)"
        )
        m = regexp.match(url)
        if m:
            return m.groups()[0]
        raise UrlNotSupported("Url not supported or wrongly formatted.")
