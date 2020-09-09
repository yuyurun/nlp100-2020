#!/usr/bin/env python
# -*- coding:utf-8 -*-

def check_value():
    
    with open('../../data/popular-names.txt', 'r') as f:
        lines = f.readlines()
    
    words = [l.split('\t')[0] for l in lines]
    return len(set(words))

if __name__ == '__main__':
    print(check_value())
