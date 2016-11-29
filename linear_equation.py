#!/usr/bin/env python3

"""数学問題: 1次方程式:

以下の方程式を解きなさい:
6x = -78
"""

#linear equation
def linear_equation():
    """1次方程式を解いていくために用意した関数

    引数:
        なし

    返り値, 戻り値:
        明示的にはなし

    単体テスト: doctest:
    >>> linear_equation()
    1次方程式: 6x = -78
    答え: x = -13
    """

    # 6x = -78
    six_num = 6
    seventy_eight_num = 78
    x_str = 'x'

    #lhs = six_num // six_num
    rhs = -seventy_eight_num // six_num
    print('1次方程式: {0}{1} = {2}\n答え: x = {3}'.format(six_num, x_str, -seventy_eight_num, rhs))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    linear_equation()

