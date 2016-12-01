#!/usr/bin/env python3

import unittest
import multi_of_6_from_1_to_100

class TestMultiOf6From1To100(unittest.TestCase):
    def test_multi_of_6_from_1_to_100(self):
        self.assertEqual(multi_of_6_from_1_to_100.multi_of_6_from_1_to_100(),
                         multi_of_6_from_1_to_100.multi_of_6_from_1_to_100())

        def m_o_6_f_1_t_100(x = 100):
            res1 = [i for i in range(1, x + 1) if i % 6 == 0]
            print('1から100までの6の倍数: {0}'.format(res1))
            length = len(res1)
            print('個数: {0}'.format(length))

        expected = m_o_6_f_1_t_100()
        actual = multi_of_6_from_1_to_100.multi_of_6_from_1_to_100()
        self.assertEqual(expected, actual)