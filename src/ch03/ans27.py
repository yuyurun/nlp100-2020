#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ans20 import extract_ing

import re

if __name__ == '__main__':
    text = extract_ing()

    lines = text.split('\n')
    pattern = re.compile('\|(.*?)\s=\s*(.*)')
    pattern2 = re.compile("'+")
    pattern3 = re.compile('\[\[(.+\||)(.+?)\]\]')

    ans = {}
    for line in lines:
        r = re.search(pattern, line)
        if r:
            rr = pattern3.sub(r'\2', r[2])
            ans[r[1]] = pattern2.sub('', rr)

    print(ans)
