#!/usr/bin/env python3

def odd_for_range(x):
    """奇数をforとrangeで出力する関数。

    奇数: 2で割り切れない整数を奇数。2で割ると余りが1。
    """

    for i in range(x):
        if i % 2 == 1:
            print(i)

if __name__ == '__main__':
    odd_for_range(10)