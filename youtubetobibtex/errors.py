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


class VideoNotFound(Exception):
    """Exception raised when not video is found with id
    """

    pass


class ChannelNotFound(Exception):
    """Exception raised when not channel is found with id
    """

    pass


class UrlNotSupported(Exception):
    """Exception raised when the id cannot be extracted from the url.
    """

    pass
