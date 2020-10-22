#! /usr/bin/env python3
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

import argparse
import sys

from youtubetobibtex.client import YoutubetobibtexClient


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="URL")
    parser.add_argument("apikey", help="API key for YouTube")
    return parser.parse_args(args)


def print_bibtex(args):
    youtube_client = YoutubetobibtexClient(args.apikey)
    if youtube_client.check():
        video_id = youtube_client.get_video_id(args.url)
        print(youtube_client.get_bibtex(video_id))
    else:
        print("Impossible to connect to the API.")
        exit()


def main():
    args = parse_args(sys.argv[1:])
    print_bibtex(args)


if __name__ == "__main__":
    main()
