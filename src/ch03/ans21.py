#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ans20 import extract_ing

if __name__ == '__main__':
    text = extract_ing()
    for line in text.split('\n'):
        if '[[Category' in line:
            print(line)
