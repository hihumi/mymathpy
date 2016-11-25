#!/usr/bin/env python3

import unittest
import even_or_odd

class TestEvenOrOdd(unittest.TestCase):
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