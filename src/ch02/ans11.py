#!/usr/bin/env python
# -*- coding:utf-8 -*-


def read_file():
    with open('../../data/popular-names.txt', 'r') as f:
        lines = f.readlines()
    return lines


if __name__ == '__main__':
    lines = read_file()
    for line in lines:
        print(line.strip('\n').replace('\t', ' '))
