#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mod_three(x):
    """3で割ったときの余りを求める関数。

    整数の分類: 整数は余りの大きさによって分類することができる。
    """

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

if __name__ == '__main__':
    mod_three(20)
