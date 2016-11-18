#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
def mod_four(x):
    #1から15までの整数を4で割った余りを出力する関数。


    counter = 0
    while counter <= x:
        if counter % 4 == 0:
            print('余り0: {0}'.format(counter))
        elif counter % 4 == 1:
            print('余り1: {0}'.format(counter))
        elif counter % 4 == 2:
            print('余り2: {0}'.format(counter))
        elif counter % 4 == 3:
            print('余り3: {0}'.format(counter))
        counter += 1

if __name__ == '__main__':
    mod_four(15)
"""

def classify_mod_four(x):
    """数値の0からnまでの整数を4で割る。余りを分類する。そして、リストで出力する関数。

    スクリプトファイル:
    問い: 0から15までの整数を4で割った余りで分類しなさい。
    答えは、この関数とスクリプト。
    """

    print('num: 0から{0}'.format(x))

    # 余り(remainder)を収めるリスト。
    r_0 = []
    r_1 = []
    r_2 = []
    r_3 = []

    counter = 0
    while counter <= x:
        if counter % 4 == 0:
            r_0.append(counter)
        elif counter % 4 == 1:
            r_1.append(counter)
        elif counter % 4 == 2:
            r_2.append(counter)
        elif counter % 4 == 3:
            r_3.append(counter)
        counter += 1
    print("余り0: {0}".format(r_0))
    print('余り1: {0}'.format(r_1))
    print('余り2: {0}'.format(r_2))
    print('余り3: {0}'.format(r_3))

if __name__ == '__main__':
    classify_mod_four(15)
