#!/usr/bin/env python3

import unittest
import le_cx_equal_n

class TestLeCXEqualN(unittest.TestCase):
    def test_le_cx_equal_n(self):
        self.assertEqual(le_cx_equal_n.le_cx_equal_n(6, -78),
                         le_cx_equal_n.le_cx_equal_n(6, -78))

        print()

        def l_c_e_n(lhs_coef, rhs_num):
            x_str = 'x'

            try:
                res = rhs_num // lhs_coef
            except ZeroDivisionError as err:
                print('{0}'.format(err))
            else:
                print('{0}{1} = {2}'.format(lhs_coef, x_str, rhs_num))
                print('{0} = {1}'.format(x_str, res))

        expected = l_c_e_n(6, -78)
        actual = le_cx_equal_n.le_cx_equal_n(6, -78)
        self.assertEqual(expected, actual)
