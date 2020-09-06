#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random


def shuffle_word_str(text):
    ans = ''
    for word in text.split():
        if len(word) > 4:
            l_word = list(word)
            create_word = l_word[0] + ''.join(random.sample(
                l_word[1:len(word)-1], len(l_word)-2)) + l_word[len(word)-1]
            ans += create_word
        else:
            ans += word
        ans += ' '

    return ans


if __name__ == '__main__':

    print('英文を入力してください.')
    input_text = input()

    print('== ランダム ==')
    print(shuffle_word_str(input_text))
