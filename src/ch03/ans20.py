#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json

def extract_ing():
    with open('../../data/jawiki-country.json') as f:
        lines = f.readlines()

    data = {}
    for line in lines:
        row = json.loads(line)
        data[row['title']] = row

    return data['イギリス']['text']
    


if __name__ == '__main__':
    print(extract_ing())
