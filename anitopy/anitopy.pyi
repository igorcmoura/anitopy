# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import List, Optional, Tuple
from typing_extensions import TypedDict

from anitopy.anitopy import default_options
default_options: ParserOptions


class ParserOptions(TypedDict, total=False):
    allowed_delimiters: str
    ignored_strings: List[str]
    parse_episode_number: bool
    parse_episode_title: bool
    parse_file_extension: bool
    parse_release_group: bool


class ParserResult(TypedDict, total=False):
    anime_title: str
    anime_year: str
    audio_term: str
    episode_number: str
    episode_title: str
    file_checksum: str
    file_extension: str
    file_name: str
    release_group: str
    release_version: str
    video_resolution: str
    video_term: str


def parse(filename: str, options: ParserOptions = default_options) -> Optional[ParserResult]: ...


def remove_extension_from_filename(filename: str) -> Tuple[str, Optional[str]]: ...


def remove_ignored_strings_from_filename(filename: str, ignored_strings: List[str]) -> str: ...
