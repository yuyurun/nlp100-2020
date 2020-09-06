#!/usr/bin/env python
# -*- coding:utf-8 -*-


def cipher(text):
    """
    与えられた文字列の各文字を，以下の仕様で変換する
    - 英小文字ならば(219 - 文字コード)の文字に置換
    - その他の文字はそのまま出力

    Args:
        text(str) : 暗号化したい文字列

    """
    ans = ''

    for i in range(len(text)):
        if text[i].islower() and text[i].isalpha:
            ans += chr(219 - ord(text[i]))
        else:
            ans += text[i]
    return ans


if __name__ == '__main__':
    print('暗号化したい文字列を入力してください.')
    input_text = input()

    print('== 暗号化 ==')
    result = cipher(input_text)
    print(result)

    print('== 復号化 ==')
    result = cipher(result)
    print(result)
