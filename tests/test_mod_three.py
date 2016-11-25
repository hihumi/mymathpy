#!/usr/bin/env python3

import unittest
import mod_three

class TestModThree(unittest.TestCase):
    def test_mod_three(self):
        self.assertEqual(mod_three.mod_three(20), mod_three.mod_three(20))
        print()

        def t_m_t(x):
            for i in range(x):
                if i % 3 == 0:
                    div_i_3_0 = i//3
                    r_0       = i%3
                    print('{0} / 3 = {1} ... {2}'.format(i, div_i_3_0, r_0))
                elif i % 3 == 1:
                    div_i_3_1 = i//3
                    r_1       = i%3
                    print('{0} / 3 = {1} ... {2}'.format(i, div_i_3_1, r_1))
                elif i % 3 == 2:
                    div_i_3_2 = i//3
                    r_2       = i%3
                    print('{0} / 3 = {1} ... {2}'.format(i, div_i_3_2, r_2))

        expected = t_m_t(20)
        actual = mod_three.mod_three(20)
        self.assertEqual(expected, actual)
