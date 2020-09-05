#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ans05 import create_ngram 


if __name__ == '__main__':
    a = 'paraparaparadise'
    b = 'paragraph'

    X = create_ngram(a)
    Y = create_ngram(b)

    print('# 和集合')
    print(set(X+Y))

    print('# 積集合')
    pro = [s for s in X if s in Y] 
    print(pro)

    print('# 差集合 X,Y')
    print([s for s in X if not s in pro])
    print([s for s in Y if not s in pro])

    print('# se in X, se in Y')
    print('se' in X)
    print('se' in Y)
