# -*- coding: utf-8 -*-


class Options:
    def __init__(self):
        self.allowed_delimiters = ' _.&+,|'
        self.ignored_strings = []

        self.parse_episode_number = True
        self.parse_episode_title = True
        self.parse_file_extension = True
        self.parse_release_group = True

default_options = Options()
