#!/usr/bin/env python3

import unittest
import lowest_common_multiple_8_12

class TestLowestCommonMultiple_8_12(unittest.TestCase):
    def test_lowest_common_multiple_8_12(self):
        self.assertEqual(lowest_common_multiple_8_12.lowest_common_multiple_8_12(50, 60), lowest_common_multiple_8_12.lowest_common_multiple_8_12(50, 60))
        print()

        def l_c_m_8_12(eight, twelve):
            common_multiple_8 = [i for i in range(1, eight + 1) if i % 8 == 0]
            common_multiple_12 = [j for j in range(1, twelve + 1) if j % 12 == 0]

            c_m_8_set = set(common_multiple_8)
            c_m_12_set = set(common_multiple_12)
            c_m_8_12_intersec = c_m_8_set.intersection(c_m_12_set)
            res = min(c_m_8_12_intersec)
            print('8と12の最小公倍数: {0}'.format(res))

        expected = l_c_m_8_12(50, 60)
        actual   = lowest_common_multiple_8_12.lowest_common_multiple_8_12(50, 60)
        self.assertEqual(expected, actual)
