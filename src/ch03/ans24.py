#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ans20 import extract_ing

import re

if __name__ == '__main__':
    text = extract_ing()
    print(re.findall(r'''
        (?:File|ファイル)
        :
        (.+?)
        \|
        ''', text, re.VERBOSE))

    """
        (?:File|ファイル)  ()のキャプチャしない版.正規表現にマッチ.
        :　　　　　　　　　: (非キャプチャ)
        (.+?)              キャプチャ対象!   . 文字, + 1回以上, ? 非貪欲マッチ
        \|　               |はor記号なのでエスケープ
    """
