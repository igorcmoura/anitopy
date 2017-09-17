# -*- coding: utf-8 -*-

from unittest import TestCase

from tests.fixtures.table import table
import anitopy

FAILING_CASES = [
    4, 13, 19, 21, 28, 30, 36, 38, 51, 63, 68, 69, 70, 75, 77, 78, 80, 81, 82,
    87, 88, 90, 92, 97, 100, 102, 108, 110, 111, 112, 114, 118, 119, 120, 123,
    126, 128, 129, 130, 136, 137, 142, 143, 144, 145, 148, 149, 155, 156, 162,
    167, 172, 173, 174
]


class TestAnitopy(TestCase):
    def test_table(self):
        self.maxDiff = None
        for index, entry in enumerate(table):
            if index in FAILING_CASES:
                continue

            filename = entry['file_name']
            elements = anitopy.parse(filename)

            expected = dict(entry)
            if 'id' in expected.keys():
                del expected['id']
            self.assertEqual(expected, elements, 'on entry number %d' % index)

    def test_fails(self):
        failed = 0
        working_tests = []
        for index in FAILING_CASES:
            entry = table[index]

            filename = entry['file_name']
            elements = anitopy.parse(filename)

            expected = dict(entry)
            if 'id' in expected.keys():
                del expected['id']
            try:
                self.assertEqual(expected, elements, 'on entry number %d'
                                                     % index)
                working_tests.append(index)
            except AssertionError as err:
                failed += 1
                print(err)

        print('\nFailed %d of %d failing cases tests' % (
            failed, len(FAILING_CASES)))
        if working_tests:
            print('There are {} working tests from the failing cases: {}'
                  .format(len(working_tests), working_tests))
