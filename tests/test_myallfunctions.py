#!/usr/bin/env python3

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
import multi_of_6_from_1_to_100
import common_multiple_4_8
import lowest_common_multiple_8_12
import one_side_of_square
import divisor_of_8

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
        self.assertEqual(even_for_range.even_for_range(10),
                         even_for_range.even_for_range(10))
        print()

        def t_e_f_r(x):
            for i in range(x):
                if i % 2 == 0:
                    print(i)

        expected = t_e_f_r(10)
        actual = even_for_range.even_for_range(10)
        self.assertEqual(expected,  actual)


    # odd_for_range
    def test_odd_for_range(self):
        self.assertEqual(odd_for_range.odd_for_range(10),
                         odd_for_range.odd_for_range(10))
        print()

        def t_o_f_r(x):
            for i in range(x):
                if i % 2 == 1:
                    print(i)

        expected = t_o_f_r(10)
        actual = odd_for_range.odd_for_range(10)
        self.assertEqual(expected, actual)


    # mod_three
    def test_mod_three(self):
        self.assertEqual(mod_three.mod_three(20),
                         mod_three.mod_three(20))
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


    # even_or_odd
    def test_even_or_odd(self):
        self.assertEqual(even_or_odd.even_or_odd(10),
                         even_or_odd.even_or_odd(10))
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
        actual = even_or_odd.even_or_odd(10)
        self.assertEqual(expected, actual)

    # classify_mod_four
    def test_classify_mod_four(self):
        self.assertEqual(classify_mod_four.classify_mod_four(15),
                         classify_mod_four.classify_mod_four(15))
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
        actual = classify_mod_four.classify_mod_four(15)
        self.assertEqual(expected, actual)

    # multi_of_seven
    def test_multi_of_seven(self):
        self.assertEqual(multi_of_seven.multi_of_seven(),
                         multi_of_seven.multi_of_seven())
        print()

        self.assertEqual(multi_of_seven.multi_of_seven(seven = 7, begin = -9, end = 9),
                         multi_of_seven.multi_of_seven(seven = 7, begin = -9, end = 9))

        def m_o_s(seven = 7, begin = 0, end = 9):
            counter = begin
            while True:
                res = seven * counter
                print('{0} * {1} = {2}'.format(seven, counter, res))
                if counter == end:
                    break
                counter += 1

        expected = m_o_s()
        actual = multi_of_seven.multi_of_seven(seven = 7, begin = 0, end = 9)
        self.assertEqual(expected, actual)


    # multi_of_6_from_1_to_100
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


    # common_multiple_4_8
    def test_common_multiple_4_8(self):
        self.assertEqual(common_multiple_4_8.common_multiple_4_8(25, 50),
                         common_multiple_4_8.common_multiple_4_8(25, 50))
        print()

        def c_m_4_8(four = 25, eight= 50):
            multiple_of_4 = [i for i in range(1, four) if i % 4 == 0]
            multiple_of_8 = [j for j in range(1, eight) if j % 8 == 0]
            print('4の倍数: {0}'.format(multiple_of_4))
            print('8の倍数: {0}'.format(multiple_of_8))

            # 以下、変数名は頭文字
            m_4_set = set(multiple_of_4)
            m_8_set = set(multiple_of_8)
            c_m_4_8_set1 = m_4_set & m_8_set
            print('4と8の公倍数(集合演算子&を使用した場合): {0}'.format(c_m_4_8_set1))
            c_m_4_8_set2 = m_4_set.intersection(m_8_set)
            print('4と8の公倍数(intersection()を使用した場合): {0}'.format(m_4_set.intersection(m_8_set)))

        expected = c_m_4_8(25, 50)
        actual = common_multiple_4_8.common_multiple_4_8(25, 50)
        self.assertEqual(expected, actual)


    # lowest_common_multiple_8_12
    def test_lowest_common_multiple_8_12(self):
        self.assertEqual(lowest_common_multiple_8_12.lowest_common_multiple_8_12(50, 60),
                         lowest_common_multiple_8_12.lowest_common_multiple_8_12(50, 60))
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
        actual = lowest_common_multiple_8_12.lowest_common_multiple_8_12(50, 60)
        self.assertEqual(expected, actual)


    # one_side_of_square
    def test_one_side_of_square(self):
        self.assertEqual(one_side_of_square.one_side_of_square(),
                         one_side_of_square.one_side_of_square())
        print()

        def o_s_o_s():

            height = 6
            width = 9

            common_multiple_6 = [i for i in range(1, 51) if i % height == 0]
            common_multiple_9 = [j for j in range(1, 51) if j % width == 0]

            c_m_6_set = set(common_multiple_6)
            c_m_9_set = set(common_multiple_9)
            res = min(c_m_6_set.intersection(c_m_9_set))
            print('正方形1辺の長さ: {0}'.format(res))

        expected = o_s_o_s()
        actual = one_side_of_square.one_side_of_square()
        self.assertEqual(expected, actual)

    # divisor_of_8
    def test_divisor_of_8(self):
        self.assertEqual(divisor_of_8.divisor_of_8(),
             divisor_of_8.divisor_of_8())
        print()

        def d_v_o_8():
            eight = 8
            res = [i for i in range(1, eight + 1) for j in range(1, eight + 1)
                   if i * j == eight]
            print('8の約数: {0}'.format(res))

        expected = d_v_o_8()
        actual = divisor_of_8.divisor_of_8()



"""
if __name__ == '__main__':
    unittest.main()
"""
