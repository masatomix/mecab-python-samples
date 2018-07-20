#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MeCab
import sys


# Mecabを用いて、形態素解析した結果を、二次元配列にして出力する
def main(args):
    # m = MeCab.Tagger("-Ochasen -d /usr/lib/mecab/dic/mecab-ipadic-neologd")
    m = MeCab.Tagger('-Ochasen')

    text = "Pythonから形態素解析エンジンMecabを呼び出してみました。"


    m.parse('')  # なんだかおまじないらしい。
    node = m.parseToNode(text)
    node = node.next # 最初はいらないので、除去

    results = []
    while node:
        word = []
        word.append(node.surface)  # 表層を追記
        word.extend(node.feature.split(","))  # 素性もカンマでsplitして、追記
        results.append(word)
        node = node.next

    results.pop() # 最後はいらないので、除去

    print(results)


# tab 区切りで出力する
def print (results):
    for line in results:
        for word in line:
            sys.stdout.write(word + "\t")
        sys.stdout.write('\n')


if __name__ == "__main__":
    main(sys.argv)
