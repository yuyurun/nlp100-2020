#!/usr/bin/env python
# -*- coding:utf-8 -*-

def split_file(n):
    
    with open('../../data/popular-names.txt', 'r') as f:
        lines = f.readlines()

    size_row = int(len(lines)//n)
    for i in range(n):
        if i == n-1:
            with open('data12/popular-names_' + str(i) + '.txt', 'w') as f:
                f.write(''.join(lines[i*size_row:]))
        else:
            with open('data12/popular-names_' + str(i) + '.txt', 'w') as f:
                f.write(''.join(lines[i*size_row:(i+1)*size_row]))

if __name__ == '__main__':
    num = int(input())
    split_file(num)
