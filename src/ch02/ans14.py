#!/usr/bin/env python
# -*- coding:utf-8 -*-

def print_head(n):
    with open('../../data/popular-names.txt', 'r') as f:
        lines = f.readlines()
    
    print(''.join(lines[:n]), end='')

if __name__ == '__main__':
    num = int(input())

    print_head(num)
