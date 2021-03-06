#!/usr/bin/env python3

import unittest
import classify_mod_four

class TestClassifyModFour(unittest.TestCase):
    def test_classify_mod_for(self):
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

