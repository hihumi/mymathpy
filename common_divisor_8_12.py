#!/usr/bin/env python3

"""算数問題: 公約数:
8と12の公約数を求めなさい。
"""

def common_divisor_8_12():
    """8と12の公約数を求める関数

    引数:
        なし

    返り値, 戻り値:
        なし

    例:
        common_divisor_8_12()
        実行結果: 8と12の公約数: {1, 2, 4}

    単体テスト: doctest:
    >>> common_divisor_8_12()
    8と12の公約数: {1, 2, 4}
    """

    eight = 8
    twelve = 12

    divisor_of_8 = [i_8 for i_8 in range(1, eight + 1)
                   for j_8 in range(1, eight + 1) if i_8 * j_8 == eight]

    divisor_of_12 = [i_12 for i_12 in range(1, twelve + 1)
                    for j_12 in range(1, twelve + 1) if i_12 * j_12 == twelve]

    # 以下、主に変数名は頭文字
    d_o_8_set = set(divisor_of_8)

    res = d_o_8_set.intersection(divisor_of_12)
    print('8と12の公約数: {0}'.format(res))


    """forで記述する場合:
    res1 = []
    for x in divisor_of_8:
        for y in divisor_of_12:
            if x == y:
                res1.append(y)
                print('ただyをforでprint: {0}'.format(y))
                continue
    print('リストとしてforを抜けた後print: {0}'.format(res1))
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    common_divisor_8_12()