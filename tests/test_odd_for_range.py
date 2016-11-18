#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import odd_for_range

class TestOddForRange(unittest.TestCase):
    def test_odd_for_range(self):
        self.assertEqual(odd_for_range.odd_for_range(10), odd_for_range.odd_for_range(10))
        print()

        def t_o_f_r(x):
            for i in range(x):
                if i % 2 == 1:
                    print(i)

        expected = t_o_f_r(10)
        actual   = odd_for_range.odd_for_range(10)
        self.assertEqual(expected, actual)
