# -*- coding: utf-8 -*-

from unittest import TestCase

from tests.fixtures.table import table
import anitopy


class TestAnitopy(TestCase):
    def test_table(self):
        for entry in table:
            tokens = anitopy.parse(entry['file_name'])
            print('"{}"'.format(entry['file_name']))
            for token in tokens:
                print(token)
            print('--------------------------------------------------')
