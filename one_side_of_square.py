#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""算数問題: 縦6cm, 横9cmの長方形のブロックを隙間なく敷き詰めて、
可能な限り小さい正方形を作りなさい。このとき、正方形の1辺の長さは何cmになるか。
"""

def one_side_of_square():
    """正方形の1辺の長さを求める関数

    引数:
        なし

    返り値, 戻り値:
        なし

    例:
        one_side_of_square()
        実行結果: 正方形1辺の長さ: 18

    単体テスト: doctest:
    >>> one_side_of_square()
    正方形1辺の長さ: 18
    """

    height = 6
    width = 9

    common_multiple_6 = [i for i in range(1, 51) if i % height == 0]
    common_multiple_9 = [j for j in range(1, 51) if j % width == 0]

    # 以下、主に変数名は頭文字を使用
    c_m_6_set = set(common_multiple_6)
    c_m_9_set = set(common_multiple_9)
    res = min(c_m_6_set.intersection(c_m_9_set))
    print('正方形1辺の長さ: {0}'.format(res))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    one_side_of_square()