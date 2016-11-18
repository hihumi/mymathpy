#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""$ python3 -m unittest -v tests.test_myallfunctions
   $ python3 -m unittest tests.test_myallfunctions
   $ python3 -m unittest -v tests.test_filename
   $ python3 -m unittest -v testdirname.test_filename
"""

import unittest

# mymodule
import even_for_range
import odd_for_range
import mod_three
import even_or_odd
import classify_mod_four
import multi_of_seven

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
        print()

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

    # classify_mod_four
    def test_classify_mod_four(self):
        self.assertEqual(classify_mod_four.classify_mod_four(15), classify_mod_four.classify_mod_four(15))
        print()

        def c_m_f(x):
            print('num: 0から{0}'.format(x))

            # 余り(remainder)を収めるリスト。
            r_0 = []
            r_1 = []
            r_2 = []
            r_3 = []

            counter = 0
            while counter <= x:
                if counter % 4 == 0:
                    r_0.append(counter)
                elif counter % 4 == 1:
                    r_1.append(counter)
                elif counter % 4 == 2:
                    r_2.append(counter)
                elif counter % 4 == 3:
                    r_3.append(counter)
                counter += 1
            print("余り0: {0}".format(r_0))
            print('余り1: {0}'.format(r_1))
            print('余り2: {0}'.format(r_2))
            print('余り3: {0}'.format(r_3))

        expected = c_m_f(15)
        actual   = classify_mod_four.classify_mod_four(15)
        self.assertEqual(expected, actual)

    # multi_of_seven
    def test_multi_of_seven(self):
        self.assertEqual(multi_of_seven.multi_of_seven(), multi_of_seven.multi_of_seven())
        print()

        self.assertEqual(multi_of_seven.multi_of_seven(seven = 7, begin = -9, end = 9), multi_of_seven.multi_of_seven(seven = 7, begin = -9, end = 9))

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


"""
if __name__ == '__main__':
    unittest.main()
"""
