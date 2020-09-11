#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ans20 import extract_ing

import re

if __name__ == '__main__':
    text = extract_ing()
    for line in text.split('\n'):
        m = re.search(r'==+.+==+', line)
        if m:
            word = m.group()
            print(word.replace('=', '').strip(), int(word.count('=')/2-1))
