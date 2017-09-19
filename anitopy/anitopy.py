# -*- coding: utf-8 -*-

from anitopy.element import Elements, ElementCategory
from anitopy.keyword import keyword_manager
from anitopy.options import default_options
from anitopy.parser import Parser
from anitopy.token import Tokens
from anitopy.tokenizer import Tokenizer


def parse(filename, options=default_options):
    Elements.clear()
    Tokens.clear()

    Elements.insert(ElementCategory.FILE_NAME, filename)
    if options.parse_file_extension:
        filename, extension = remove_extension_from_filename(filename)
        if extension:
            Elements.insert(ElementCategory.FILE_EXTENSION, extension)

    if options.ignored_strings:
        filename = remove_ignored_strings_from_filename(
            filename, options.ignored_strings
        )

    if not filename:
        return None

    tokenizer = Tokenizer(filename, options)
    if not tokenizer.tokenize():
        return None

    parser = Parser(options)
    if not parser.parse():
        return None

    return Elements.get_dictionary()


def remove_extension_from_filename(filename):
    split_filename = filename.rsplit('.', 1)

    if len(split_filename) < 2:
        return filename, None

    new_filename, extension = split_filename

    max_length = 4
    if len(extension) > max_length:
        return filename, None

    if not extension.isalnum():
        return filename, None

    keyword = keyword_manager.normalize(extension)
    if not keyword_manager.find(keyword, ElementCategory.FILE_EXTENSION):
        return filename, None

    return new_filename, extension


def remove_ignored_strings_from_filename(filename, ignored_strings):
    for string in ignored_strings:
        filename = filename.replace(string, '')
    return filename
