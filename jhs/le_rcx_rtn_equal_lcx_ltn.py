#!/usr/bin/env python3

"""数学問題: 1次方程式:
6x - 12 = 24
また
-2x - 7 = -6x + 21
を解く関数を作成しなさい
"""

def le_rcx_rtn_equal_lcx_ltn(rhs_coef_x = 0, rhs_term_n = 0,
                             lhs_coef_x = 0, lhs_term_n = 0):
    """6x - 12 = 24 また、-2x - 7 = -6x + 21のような1次方程式を解く関数

    引数:
        rhs_coerf_x: 左辺xの係数。初期値は0
        rhs_term_n: 左辺の項n。初期値は0
        lhs_coef_x: 右辺xの係数。初期値は0
        lhs_term_n: 右辺の項n。初期値は0

    返り値, 戻り値:
        明示的にはなし

    例: le_rcx_rtn_equal_lcx_ltn(-2, -7, -6, 21)
        実行結果: x = 7

    単体テスト: doctest:
    >>> le_rcx_rtn_equal_lcx_ltn(rhs_coef_x = -2, rhs_term_n = -7, lhs_coef_x = -6, lhs_term_n = 21)
    x = 7
    >>> le_rcx_rtn_equal_lcx_ltn(6, -12, 0, 24)
    x = 6
    """

    rhs = rhs_coef_x + (-lhs_coef_x)
    lhs = lhs_term_n + (-rhs_term_n)

    try:
        res = lhs // rhs
    except (TypeError, ValueError, ZeroDivisionError) as err:
        print('error: {0}'.format(err))
    else:
        print('x = {0}'.format(res))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    le_rcx_rtn_equal_lcx_ltn(rhs_coef_x = -2, rhs_term_n = -7,
                             lhs_coef_x = -6, lhs_term_n = 21)
    le_rcx_rtn_equal_lcx_ltn(6, -12, 0, 24)
