#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""$ python3 -m unittest -v tests.test_myallfunctions
   $ python3 -m unittest tests.test_myallfunctions
   $ python3 -m unittest -v tests.test_filename
   $ python3 -m unittest -v testdirname.test_filename
"""

import unittest

import even_for_range
import odd_for_range
import mod_three
import even_or_odd

class TestMyAllFunctions(unittest.TestCase):

    # test_funcs_name
    """
    def test_new_func(self):
        self.assert___


        NOTE: Indent
        def t_n_f():
           do something

        expected = ___
        actual   = ___
        self.assert___

    """

    # even_for_range
    def test_even_for_range(self):
        self.assertEqual(even_for_range.even_for_range(10), even_for_range.even_for_range(10))
        print()

        def t_e_f_r(x):
            for i in range(x):
                if i % 2 == 0:
                    print(i)

        expected = t_e_f_r(10)
        actual   = even_for_range.even_for_range(10)
        self.assertEqual(expected,  actual)


    # odd_for_range
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


    # mod_three
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
        actual   = mod_three.mod_three(20)
        self.assertEqual(expected, actual)


    # even_or_odd
    def test_even_or_odd(self):
        self.assertEqual(even_or_odd.even_or_odd(10), even_or_odd.even_or_odd(10))

        def t_e_o_o(x):
            counter = 0
            while counter <= x:
                if counter % 2 == 0:
                    print('even num: {0}'.format(counter))
                else:
                    print('odd num: {0}'.format(counter))
                counter += 1

        expected = t_e_o_o(10)
        actual   = even_or_odd.even_or_odd(10)
        self.assertEqual(expected, actual)

"""
if __name__ == '__main__':
    unittest.main()
"""