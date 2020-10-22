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

import datetime
import io
import sys
import unittest
from unittest import TestCase

from youtubetobibtex.cli import parse_args, print_bibtex
from youtubetobibtex.client import YoutubetobibtexClient
from youtubetobibtex.errors import UrlNotSupported, VideoNotFound


class YoutubeToBibtexClientTests(TestCase):
    def setUp(self):
        try:
            f = open(".apikeytest", "r")
            self.creds = f.read()
        except Exception as e:
            raise Exception(
                "You must provide credentials through the .apikeytest file : {}".format(
                    e
                )
            )
        self.client = YoutubetobibtexClient(self.creds)

    def test_api_not_valid(self):
        client = YoutubetobibtexClient("false api key")
        self.assertFalse(client.check())

    def test_client(self):
        video_url = "https://www.youtube.com/watch?v=_kLb1glm6EM"
        self.assertTrue(self.client.check())
        self.assertEqual(
            self.client.get_video_id("https://www.youtube.com/watch?v=_kLb1glm6EM"),
            "_kLb1glm6EM",
        )
        self.assertEqual(
            self.client._get_video_info("_kLb1glm6EM"),
            (
                "The Quantum Prisoner's Dilemma (ft. Physics Girl!)",
                "Up and Atom",
                datetime.datetime(2018, 3, 22, 11, 56, 12),
            ),
        )
        expected_bibtex = """
@online{video:upandatom2018,
    title = {The Quantum Prisoner's Dilemma (ft. Physics Girl!)},
    date = {2018},
    organization = {YouTube},
    author = {Up and Atom},
    url = {https://youtube.com/watch?v=_kLb1glm6EM},
}
        """
        self.assertEqual(self.client.get_bibtex("_kLb1glm6EM"), expected_bibtex)

    def test_exceptions(self):
        with self.assertRaises(UrlNotSupported):
            self.client.get_video_id("https://google.com")
        with self.assertRaises(VideoNotFound):
            self.client._get_video_info("falseid")


class YoutubeToBibtexCliTests(TestCase):
    def setUp(self):
        self.url = "https://www.youtube.com/watch?v=_kLb1glm6EM"
        try:
            f = open(".apikeytest", "r")
            self.creds = f.read()
        except Exception as e:
            raise Exception(
                "You must provide credentials through the .apikeytest file : {}".format(
                    e
                )
            )
        self.args = [self.url, self.creds]

    def test_parser(self):
        parsed_args = parse_args(self.args)
        self.assertEqual(parsed_args.url, self.url)
        self.assertEqual(parsed_args.apikey, self.creds)

    def test_cli(self):
        parsed_args = parse_args(self.args)
        expected_bibtex = """\n@online{video:upandatom2018,\n    title = {The Quantum Prisoner's Dilemma (ft. Physics Girl!)},\n    date = {2018},\n    organization = {YouTube},\n    author = {Up and Atom},\n    url = {https://youtube.com/watch?v=_kLb1glm6EM},\n}\n        \n"""
        output = io.StringIO()
        sys.stdout = output
        print_bibtex(parsed_args)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_bibtex)

    def test_error(self):
        parsed_args = parse_args([self.url, "plop"])
        output = io.StringIO()
        sys.stdout = output
        with self.assertRaises(SystemExit):
            print_bibtex(parsed_args)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "Impossible to connect to the API.\n")


if __name__ == "__main__":
    unittest.main()
