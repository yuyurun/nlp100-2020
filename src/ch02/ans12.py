#!/usr/bin/env python
# -*- coding:utf-8 -*-


def create_split_file(col_id):
    with open('../../data/popular-names.txt', 'r') as f:
        lines = f.readlines()

    with open('data12/col' + str(col_id) + '.txt', 'w') as f:
        f.write('\n'.join([l.split('\t')[col_id-1] for l in lines]))
        f.write('\n')


if __name__ == '__main__':
    create_split_file(1)
    create_split_file(2)
