#!/usr/bin/env python3

import unittest
import common_divisor_8_12

class TestCommonDivisor_8_12(unittest.TestCase):
    def test_common_divisor_8_12(self):
        self.assertEqual(common_divisor_8_12.common_divisor_8_12(),
                         common_divisor_8_12.common_divisor_8_12()),
        print()


        def c_d_8_12():
            eight = 8
            twelve = 12

            divisor_of_8 = [i_8 for i_8 in range(1, eight + 1)
                           for j_8 in range(1, eight + 1) if i_8 * j_8 == eight]

            divisor_of_12 = [i_12 for i_12 in range(1, twelve + 1)
                             for j_12 in range(1, twelve + 1) if i_12 * j_12 == twelve]

            # 以下、主に変数名は頭文字
            d_o_8_set = set(divisor_of_8)

            res = d_o_8_set.intersection(divisor_of_12)
            print('8と12の公約数: {0}'.format(res))

        expected = c_d_8_12()
        actual = common_divisor_8_12.common_divisor_8_12()
        self.assertEqual(expected, actual)

