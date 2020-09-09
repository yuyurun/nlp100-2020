#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pandas as pd


def sort_by_colomn1():
    df = pd.read_csv('../../data/popular-names.txt', sep='\t', header=None)

    words = list(df[0].value_counts().index)
    df['order'] = df[0].apply(lambda x: words.index(x) if x in words else -1)
    
    df = df.sort_values('order')
    for i, v in df.iterrows():
        print('{}\t{}\t{}\t{}'.format(v[0], v[1], v[2], v[3]))
    

if __name__ == '__main__':
    sort_by_colomn1()
