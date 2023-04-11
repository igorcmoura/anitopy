# -*- coding: utf-8 -*-

from __future__ import annotations

from enum import Enum
from typing import Literal

from anitopy.anitopy import ParserResult


class ElementCategory(Enum):
    ANIME_SEASON = Literal['anime_season']
    ANIME_SEASON_PREFIX = Literal['anime_season_prefix']
    ANIME_TITLE = Literal['anime_title']
    ANIME_TYPE = Literal['anime_type']
    ANIME_YEAR = Literal['anime_year']
    AUDIO_TERM = Literal['audio_term']
    DEVICE_COMPATIBILITY = Literal['device_compatibility']
    EPISODE_NUMBER = Literal['episode_number']
    EPISODE_NUMBER_ALT = Literal['episode_number_alt']
    EPISODE_PREFIX = Literal['episode_prefix']
    EPISODE_TITLE = Literal['episode_title']
    FILE_CHECKSUM = Literal['file_checksum']
    FILE_EXTENSION = Literal['file_extension']
    FILE_NAME = Literal['file_name']
    LANGUAGE = Literal['language']
    OTHER = Literal['other']
    RELEASE_GROUP = Literal['release_group']
    RELEASE_INFORMATION = Literal['release_information']
    RELEASE_VERSION = Literal['release_version']
    SOURCE = Literal['source']
    SUBTITLES = Literal['subtitles']
    VIDEO_RESOLUTION = Literal['video_resolution']
    VIDEO_TERM = Literal['video_term']
    VOLUME_NUMBER = Literal['volume_number']
    VOLUME_PREFIX = Literal['volume_prefix']
    UNKNOWN = Literal['unknown']

    @classmethod
    def is_searchable(cls, category: ElementCategory) -> bool: ...

    @classmethod
    def is_singular(cls, category: ElementCategory) -> bool: ...


class Elements:
    _elements: dict[str, list[str]]
    _check_alt_number: bool

    def __init__(self) -> None: ...

    def get_check_alt_number(self) -> bool: ...

    def set_check_alt_number(self, value: bool) -> None: ...

    def insert(self, category: ElementCategory, content: str) -> None: ...

    def erase(self, category: ElementCategory) -> None: ...

    def remove(self, category: ElementCategory, content: str) -> None: ...

    def contains(self, category: ElementCategory) -> bool: ...

    def empty(self) -> bool: ...

    def get(self, category: ElementCategory) -> str | list[str]: ...

    def get_dictionary(self) -> ParserResult: ...
