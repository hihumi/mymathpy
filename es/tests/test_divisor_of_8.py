#!/usr/bin/env python3

import unittest
import divisor_of_8

class TestDivisorOf8(unittest.TestCase):
    def test_divisor_of_8(self):
        self.assertEqual(divisor_of_8.divisor_of_8(),
             divisor_of_8.divisor_of_8())
        print()

        def d_v_o_8():
            eight = 8
            res = [i for i in range(1, eight + 1) for j in range(1, eight + 1)
                   if i * j == eight]
            print('8の約数: {0}'.format(res))

        expected = d_v_o_8()
        actual = divisor_of_8.divisor_of_8()
        self.assertEqual(expected, actual)
