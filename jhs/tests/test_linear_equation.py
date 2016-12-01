#!/usr/bin/env python3

import unittest
import linear_equation

class TestLinearEquation(unittest.TestCase):
    def test_linear_equation(self):
        self.assertEqual(linear_equation.linear_equation(),
                         linear_equation.linear_equation())

        # 6x = -78
        def l_e_1():
            six_num = 6
            seventy_eight_num = 78
            x_str = 'x'

            rhs = -seventy_eight_num // six_num
            print('1次方程式: {0}{1} = {2}\n答え: x = {3}'.format(six_num, x_str, -seventy_eight_num, rhs))

        expected = l_e_1()
        actual = linear_equation.linear_equation()
        self.assertEqual(expected, actual)
