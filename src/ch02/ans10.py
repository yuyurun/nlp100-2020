#!/usr/bin/env python
# -*- coding:utf-8 -*-

def calc_wc(fname):
    with open(fname, 'r') as f:
        lines = f.readlines()
    return len(lines)

if __name__ == '__main__':
    print(calc_wc('../../data/popular-names.txt'))


