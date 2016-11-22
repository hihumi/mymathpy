#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def common_multiple_4_8(four = 25, eight= 50):
    """4の倍数と8の倍数と公倍数を出力する関数。

    問い: 4と8の倍数を求め、公倍数を見つけなさい。
    """
    multiple_of_4 = [i for i in range(1, four) if i % 4 == 0]
    multiple_of_8 = [j for j in range(1, eight) if j % 8 == 0]
    print('4の倍数: {0}'.format(multiple_of_4))
    print('8の倍数: {0}'.format(multiple_of_8))

    # 以下、変数名は頭文字
    m_4_set = set(multiple_of_4)
    m_8_set = set(multiple_of_8)
    c_m_4_8_set1 = m_4_set & m_8_set
    print('4と8の公倍数(集合演算子&を使用した場合): {0}'.format(c_m_4_8_set1))
    c_m_4_8_set2 = m_4_set.intersection(m_8_set)
    print('4と8の公倍数(intersection()を使用した場合): {0}'.format(m_4_set.intersection(m_8_set)))

if __name__ == '__main__':
    common_multiple_4_8(25, 50)