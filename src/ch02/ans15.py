#!/usr/bin/env python
# -*- coding:utf-8 -*-

def print_tail(n):
    with open('../../data/popular-names.txt', 'r') as f:
        lines = f.readlines()
    
    print(''.join(lines[len(lines)-n:]), end='')

if __name__ == '__main__':
    num = int(input())

    print_tail(num)
