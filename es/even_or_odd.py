#!/usr/bin/env python3

def even_or_odd(x):
    """ 整数を、偶数か奇数かで出力する関数。

    関数の数値を、whileでその数値まで1ずつ増分させながら、2で割り切れたら偶数、そうでなければ奇数。
    """

    counter = 0
    while counter <= x:
        if counter % 2 == 0:
            print('even num: {0}'.format(counter))
        else:
            print('odd num: {0}'.format(counter))
        counter += 1

if __name__ == '__main__':
    even_or_odd(10)