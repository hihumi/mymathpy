#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import multi_of_seven

class TestMultiOfSeven(unittest.TestCase):
    def test_multi_of_seven(self):
        self.assertEqual(multi_of_seven.multi_of_seven(), multi_of_seven.multi_of_seven())
        print()

        self.assertEqual(multi_of_seven.multi_of_seven(seven = 7, begin = -9, end = 9), multi_of_seven.multi_of_seven(seven = 7, begin = -9, end = 9))
        print()

        def m_o_s(seven = 7, begin = 0, end = 9):
            counter = begin
            while True:
                res = seven * counter
                print('{0} * {1} = {2}'.format(seven, counter, res))
                if counter == end:
                    break
                counter += 1

        expected = m_o_s()
        actual   = multi_of_seven.multi_of_seven(seven = 7, begin = 0, end = 9)
        self.assertEqual(expected, actual)
