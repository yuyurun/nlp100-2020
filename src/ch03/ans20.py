#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json


if __name__ == '__main__':
    with open('../../data/jawiki-country.json') as f:
        lines = f.readlines()

    data = {}
    for line in lines:
        row = json.loads(line)
        data[row['title']] = row

    print(data['イギリス']['text'])
