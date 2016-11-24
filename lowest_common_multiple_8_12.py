#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""算数問題: 8と12の最小公倍数を求めなさい。
"""

def lowest_common_multiple_8_12(eight, twelve):
    """8と12の最小公倍数を求める関数

    引数:
        eight: 8の倍数を求めるための数値
        twelve: 12の倍数を求めるための数値
    例:
        common_multiple_8_12(50, 60)
        引数の数値50が8の倍数を50まで求める。
        引数の数値60が12の倍数を60まで求める。
        実行結果: 8と12の最小公倍数: 24

    単体テスト: doctest:
    >>> lowest_common_multiple_8_12(50, 60)
    8と12の最小公倍数: 24
    """

    common_multiple_8 = [i for i in range(1, eight + 1) if i % 8 == 0]
    common_multiple_12 = [j for j in range(1, twelve + 1) if j % 12 == 0]

    # 以下、主に変数名は頭文字を使用
    c_m_8_set = set(common_multiple_8)
    c_m_12_set = set(common_multiple_12)
    c_m_8_12_intersec = c_m_8_set.intersection(c_m_12_set)
    res = min(c_m_8_12_intersec)
    print('8と12の最小公倍数: {0}'.format(res))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    lowest_common_multiple_8_12(50, 60)

