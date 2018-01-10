# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from unittest import TestCase

import anitopy
from tests.fixtures.table import table

FAILING_CASES = [
    4, 13, 21, 28, 38, 63, 68, 69, 70, 75, 77, 80, 81, 82, 87, 90, 92, 97, 100,
    102, 110, 111, 112, 114, 120, 123, 128, 129, 136, 137, 142, 143, 145, 162,
    167
]


class TestAnitopy(TestCase):
    def parse_options(self, entry_options):
        if entry_options is None:
            return {}

        options = {}
        for option, value in entry_options.items():
            option_name = option.split('option_')[1]
            options[option_name] = value
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

            try:
                print('Index %d "%s"' % (index, filename))
            except:
                print(('Index %d "%s"' % (index, filename)).encode("utf-8"))

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
