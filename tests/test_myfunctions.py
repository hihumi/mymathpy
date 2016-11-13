#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""$ python3 -m unittest -v tests.test_myfunctions
"""

import unittest
import even_for_range

class TestMyFunctions(unittest.TestCase):

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

    # other
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




