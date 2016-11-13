#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def even_for_range(x):
    """偶数をforとrangeで出力する関数。

    偶数: 2で割り切れる整数を偶数。2で割ると余りが0。
    """

    for i in range(x):
        if i % 2 == 0:
            print(i)

if __name__ == '__main__':
    even_for_range(10)

