#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import one_side_of_square

class TestOneSideOfSquare(unittest.TestCase):
    def test_one_side_of_square(self):
        self.assertEqual(one_side_of_square.one_side_of_square(), one_side_of_square.one_side_of_square())
        print()

        def o_s_o_s():

            height = 6
            width  = 9

            common_multiple_6 = [i for i in range(1, 51) if i % height == 0]
            common_multiple_9 = [j for j in range(1, 51) if j % width == 0]

            c_m_6_set = set(common_multiple_6)
            c_m_9_set = set(common_multiple_9)
            res = min(c_m_6_set.intersection(c_m_9_set))
            print('正方形1辺の長さ: {0}'.format(res))

        expected = o_s_o_s()
        actual   = one_side_of_square.one_side_of_square()
        self.assertEqual(expected, actual)

