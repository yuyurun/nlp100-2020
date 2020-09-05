#!/usr/bin/env python
# -*- coding:utf-8 -*-


def create_sentence_xyz(x, y, z):
    return "{}時の{}は{}".format(x, y, z)


if __name__ == '__main__':
    print(create_sentence_xyz(12, "気温", 22.4))
