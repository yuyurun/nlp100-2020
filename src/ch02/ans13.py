#!/usr/bin/env python
# -*- coding:utf-8 -*-


def merge_col_file():
    with open('data12/col1.txt', 'r') as f:
        lines1 = f.readlines()

    with open('data12/col2.txt', 'r') as f:
        lines2 = f.readlines()

    with open('data12/col12.txt', 'w') as f:
        f.write('\n'.join([lines1[i].strip('\n') + '\t' + lines2[i].strip('\n')
                           for i in range(len(lines1))]))
        f.write('\n')


if __name__ == '__main__':
    merge_col_file()
