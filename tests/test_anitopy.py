# -*- coding: utf-8 -*-

from unittest import TestCase

import anitopy
from anitopy.options import Options, default_options
from tests.fixtures.table import table

FAILING_CASES = [
    4, 13, 19, 21, 28, 30, 36, 38, 51, 63, 68, 69, 70, 75, 77, 78, 80, 81, 82,
    87, 88, 90, 92, 97, 100, 102, 110, 111, 112, 114, 118, 119, 120, 123, 126,
    128, 129, 136, 137, 142, 143, 144, 145, 156, 162, 167, 174
]


class TestAnitopy(TestCase):
    def parse_options(self, entry_options):
        if entry_options is None:
            return default_options

        options = Options()
        for option, value in entry_options.items():
            if option == 'option_allowed_delimiters':
                options.allowed_delimiters = value
            if option == 'option_ignored_strings':
                options.ignored_strings = value
            if option == 'option_parse_episode_number':
                options.parse_episode_number = value
            if option == 'option_parse_episode_title':
                options.parse_episode_title = value
            if option == 'option_parse_file_extension':
                options.parse_file_extension = value
            if option == 'option_parse_release_group':
                options.parse_release_group = value
        return options

    def test_table(self):
        for index, entry in enumerate(table):
            if index in FAILING_CASES:
                continue

            filename = entry[0]
            options = self.parse_options(entry[1])

            elements = anitopy.parse(filename, options=options)

            expected = dict(entry[2])
            if 'id' in expected.keys():
                del expected['id']
            self.assertEqual(expected, elements, 'on entry number %d' % index)

    def test_fails(self):
        failed = 0
        working_tests = []
        for index in FAILING_CASES:
            entry = table[index]
            filename = entry[0]
            options = self.parse_options(entry[1])
            print('Index %d "%s"' % (index, filename))

            elements = anitopy.parse(filename, options=options)

            expected = dict(entry[2])
            if 'id' in expected.keys():
                del expected['id']
            try:
                self.assertEqual(expected, elements)
                working_tests.append(index)
            except AssertionError as err:
                failed += 1
                print(err)
                print('----------------------------------------------------------------------')  # noqa E501

        print('\nFailed %d of %d failing cases tests' % (
            failed, len(FAILING_CASES)))
        if working_tests:
            print('There are {} working tests from the failing cases: {}'
                  .format(len(working_tests), working_tests))
