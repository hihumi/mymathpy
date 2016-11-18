#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multi_of_seven(seven = 7, begin = 0, end = 9):
    """7の倍数、7の整数倍を出力する関数。

    """

    counter = begin
    while True:
            res = seven * counter
            print('{0} * {1} = {2}'.format(seven, counter, res))
            if counter == end:
                break
            counter += 1

if __name__ == '__main__':
    multi_of_seven()
    print()
    multi_of_seven(seven = 7, begin = -9, end = 9)
    print()
    multi_of_seven(7, -9, 9)
    print()
    multi_of_seven(7, 1, 9)
    print()
    multi_of_seven(7, 0, 2)
