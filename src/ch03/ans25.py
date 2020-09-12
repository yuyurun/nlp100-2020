#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ans20 import extract_ing

import re

if __name__ == '__main__':
    text = extract_ing()

    lines = text.split('\n')
    pattern = re.compile('\|(.*?)\s=\s*(.*)')

    ans = {}
    for line in lines:
        r = re.search(pattern, line)
        if r:
            ans[r[1]] = r[2]

    print(ans)
        
