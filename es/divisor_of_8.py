#!/usr/bin/env python3

"""算数問題: 約数:

約数とは、整数xを割り切ることができる整数xのこという。
例えば、8の約数は、1とその数自身である8も含まれる。
8の約数をすべて求めなさい。
"""
def divisor_of_8():
    """8の約数をすべて出力する関数。

    引数:
        なし

    返り値, 戻り値:
        なし

    例:
        divisor_of_8()
        実行結果: 8の約数: [1, 2, 4, 8]

    単体テスト: doctest:
    >>> divisor_of_8()
    8の約数: [1, 2, 4, 8]
    """

    eight = 8
    res = [i for i in range(1, eight + 1) for j in range(1, eight + 1)
           if i * j == eight]
    print('8の約数: {0}'.format(res))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    divisor_of_8()