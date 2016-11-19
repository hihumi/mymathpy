#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multi_of_6_from_1_to_100(x = 100):
    """1から100までの整数から6の倍数を出力する関数

    問い: 1から100までの整数に6の倍数は何個あるか。
    """

    """ for文
    res = []
    for i in range(1, x + 1):
        if i % 6 == 0:
            res.append(i)
    print(res)
    print(len(res))
    """

    res1 = [i for i in range(1, x + 1) if i % 6 == 0]
    print('1から100までの6の倍数: {0}'.format(res1))
    length = len(res1)
    print('個数: {0}'.format(length))

if __name__ == '__main__':
    multi_of_6_from_1_to_100()
