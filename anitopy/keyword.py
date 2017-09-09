# -*- coding: utf-8 -*-

from anitopy.element import ElementCategory


class KeywordOption:
    def __init__(self, identifiable=True, searchable=True, valid=True):
        self.identifiable = identifiable
        self.searchable = searchable
        self.valid = valid


class Keyword:
    def __init__(self, category, options):
        self.category = category
        self.options = options


class KeywordManager:
    def __init__(self):
        options_default = KeywordOption()
        options_invalid = KeywordOption(True, True, False)
        options_unidentifiable = KeywordOption(False, True, True)
        options_unidentifiable_invalid = KeywordOption(False, True, False)
        options_unidentifiable_unsearchable = KeywordOption(False, False, True)

        self._file_extensions = {}
        self._keys = {}

        self.add(ElementCategory.ANIME_SEASON_PREFIX, options_unidentifiable, [
            'SAISON', 'SEASON'])

        self.add(ElementCategory.ANIME_TYPE, options_unidentifiable, [
            'GEKIJOUBAN', 'MOVIE',
            'OAD', 'OAV', 'ONA', 'OVA',
            'SPECIAL', 'SPECIALS',
            'TV'])
        self.add(ElementCategory.ANIME_TYPE,
                 options_unidentifiable_unsearchable,
                 ['SP'])  # e.g. "Yumeiro Patissiere SP Professional"
        self.add(ElementCategory.ANIME_TYPE, options_unidentifiable_invalid, [
            'ED', 'ENDING', 'NCED',
            'NCOP', 'OP', 'OPENING',
            'PREVIEW', 'PV'])

        self.add(ElementCategory.AUDIO_TERM, options_default, [
            # Audio channels
            '2.0CH', '2CH', '5.1', '5.1CH', 'DTS', 'DTS-ES', 'DTS5.1',
            'TRUEHD5.1',
            # Audio codec
            'AAC', 'AACX2', 'AACX3', 'AACX4', 'AC3', 'FLAC', 'FLACX2',
            'FLACX3', 'FLACX4', 'LOSSLESS', 'MP3', 'OGG', 'VORBIS',
            # Audio language
            'DUALAUDIO', 'DUAL AUDIO'])

        self.add(ElementCategory.DEVICE_COMPATIBILITY, options_default, [
            'IPAD3', 'IPHONE5', 'IPOD', 'PS3', 'XBOX', 'XBOX360'])
        self.add(ElementCategory.DEVICE_COMPATIBILITY, options_unidentifiable,
                 ['ANDROID'])

        self.add(ElementCategory.EPISODE_PREFIX, options_default, [
            'EP', 'EP.', 'EPS', 'EPS.', 'EPISODE', 'EPISODE.', 'EPISODES',
            'CAPITULO', 'EPISODIO', 'FOLGE'])
        self.add(ElementCategory.EPISODE_PREFIX, options_invalid, [
            'E', '\x7B2C'])  # single-letter episode keywords are not valid

        self.add(ElementCategory.FILE_EXTENSION, options_default, [
            '3GP', 'AVI', 'DIVX', 'FLV', 'M2TS', 'MKV', 'MOV', 'MP4', 'MPG',
            'OGM', 'RM', 'RMVB', 'WEBM', 'WMV'])
        self.add(ElementCategory.FILE_EXTENSION, options_invalid, [
            'AAC', 'AIFF', 'FLAC', 'M4A', 'MP3', 'MKA', 'OGG', 'WAV', 'WMA',
            '7Z', 'RAR', 'ZIP',
            'ASS', 'SRT'])

        self.add(ElementCategory.LANGUAGE, options_default, [
            'ENG', 'ENGLISH', 'ESPANOL', 'JAP', 'PT-BR', 'SPANISH', 'VOSTFR'])
        self.add(ElementCategory.LANGUAGE, options_unidentifiable, [
            'ESP', 'ITA'])  # e.g. "Tokyo ESP", "Bokura ga Ita"

        self.add(ElementCategory.OTHER, options_default, [
            'REMASTER', 'REMASTERED', 'UNCENSORED', 'UNCUT',
            'TS', 'VFR', 'WIDESCREEN', 'WS'])

        self.add(ElementCategory.RELEASE_GROUP, options_default, [
            'THORA'])

        self.add(ElementCategory.RELEASE_INFORMATION, options_default, [
            'BATCH', 'COMPLETE', 'PATCH', 'REMUX'])
        self.add(ElementCategory.RELEASE_INFORMATION, options_unidentifiable, [
            'END', 'FINAL'])  # e.g. "The End of Evangelion", "Final Approach"

        self.add(ElementCategory.RELEASE_VERSION, options_default, [
            'V0', 'V1', 'V2', 'V3', 'V4'])

        self.add(ElementCategory.SOURCE, options_default, [
            'BD', 'BDRIP', 'BLURAY', 'BLU-RAY',
            'DVD', 'DVD5', 'DVD9', 'DVD-R2J', 'DVDRIP', 'DVD-RIP',
            'R2DVD', 'R2J', 'R2JDVD', 'R2JDVDRIP',
            'HDTV', 'HDTVRIP', 'TVRIP', 'TV-RIP',
            'WEBCAST', 'WEBRIP'])

        self.add(ElementCategory.SUBTITLES, options_default, [
            'ASS', 'BIG5', 'DUB', 'DUBBED', 'HARDSUB', 'RAW', 'SOFTSUB',
            'SOFTSUBS', 'SUB', 'SUBBED', 'SUBTITLED'])

        self.add(ElementCategory.VIDEO_TERM, options_default, [
            # Frame rate
            '23.976FPS', '24FPS', '29.97FPS', '30FPS', '60FPS', '120FPS',
            # Video codec
            '8BIT', '8-BIT',
            '10BIT', '10BITS', '10-BIT', '10-BITS', 'HI10', 'HI10P',
            'H264', 'H265', 'H.264', 'H.265', 'X264', 'X265', 'X.264',
            'AVC', 'HEVC', 'DIVX', 'DIVX5', 'DIVX6', 'XVID',
            # Video format
            'AVI', 'RMVB', 'WMV', 'WMV3', 'WMV9',
            # Video quality
            'HQ', 'LQ',
            # Video resolution
            'HD', 'SD'])

        self.add(ElementCategory.VOLUME_PREFIX, options_default, [
            'VOL', 'VOL.', 'VOLUME'])

    def add(self, category, options, keywords):
        keyword_container = self._get_keyword_container(category)
        for keyword in keywords:
            if not keyword:
                continue
            if keyword in keyword_container.keys():
                continue
            keyword_container[keyword] = Keyword(category, options)

    def find(self, string, category=ElementCategory.UNKNOWN):
        keyword_container = self._get_keyword_container(category)
        if string not in keyword_container.keys():
            return None
        keyword = keyword_container[string]
        if category != ElementCategory.UNKNOWN and \
                keyword.category != category:
            return None
        return keyword

    @staticmethod
    def normalize(string):
        return string.upper()

    def _get_keyword_container(self, category):
        return self._file_extensions \
               if category == ElementCategory.FILE_EXTENSION \
               else self._keys


keyword_manager = KeywordManager()
