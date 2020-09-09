#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pandas as pd


def sort_by_colomn3():
    df = pd.read_csv('../../data/popular-names.txt', sep='\t', header=None)

    df = df.sort_values(2)
    for i, v in df.iterrows():
        print('{}\t{}\t{}\t{}'.format(v[0], v[1], v[2], v[3]))


if __name__ == '__main__':
    sort_by_colomn3()
