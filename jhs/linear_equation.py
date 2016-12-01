#!/usr/bin/env python3

"""数学問題: 1次方程式:

以下の方程式を解きなさい:
6x = -78
-11x = -132
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
    1次方程式:
    <BLANKLINE>
    6x = -78
    答え: x = -13
    <BLANKLINE>
    -11x = 132
    答え: x = 12
    """

    print('1次方程式:')
    print()

    x_str = 'x'

    # 6x = -78
    six_num = 6
    seventy_eight_num = 78

    # lhs = six_num // six_num
    rhs1 = -seventy_eight_num // six_num
    print('{0}{1} = {2}'.format(six_num, x_str, -seventy_eight_num))
    print('答え: {0} = {1}'.format(x_str, rhs1))
    print()


    # -11x = -132
    eleven_num = 11
    onehundred_thirtytwo = 132
    rhs2 = -onehundred_thirtytwo // -eleven_num
    print('{0}{1} = {2}'.format(-eleven_num, x_str, onehundred_thirtytwo))
    print('答え: {0} = {1}'.format(x_str, rhs2))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    linear_equation()

