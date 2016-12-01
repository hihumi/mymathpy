#!/usr/bin/env python3

"""数学問題: 1次方程式
6x = -78 を解くような汎用的な関数を作成しなさい
"""

def le_cx_equal_n(lhs_coef, rhs_num):
    """6x = -78 のような1次方程式を解く関数

    引数:
        lhs_coef: 左辺の係数
        rhs_num: 右辺の値

    返り値, 戻り値:
        明示的にはなし

    例:
        le_cx_equal_n(6, -78)
        実行結果: 6x = -78
                  x = -13

    単体テスト: doctest:
    >>> le_cx_equal_n(6, -78)
    6x = -78
    x = -13

    >>> le_cx_equal_n(-11, -132)
    -11x = -132
    x = 12

    >>> le_cx_equal_n(-9, 117)
    -9x = 117
    x = -13

    >>> le_cx_equal_n(-7, 147)
    -7x = 147
    x = -21
    """

    x_str = 'x'

    try:
        res = rhs_num // lhs_coef
    except (TypeError, ValueError, ZeroDivisionError) as err:
        print('{0}'.format(err))
    else:
        print('{0}{1} = {2}'.format(lhs_coef, x_str, rhs_num))
        print('{0} = {1}'.format(x_str, res))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    le_cx_equal_n(6, -78)
    print()
    le_cx_equal_n(-11, -132)
    print()
    le_cx_equal_n(-9, 117)
    print()
    le_cx_equal_n(-7, 147)
