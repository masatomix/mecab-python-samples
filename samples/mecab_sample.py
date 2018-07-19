#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MeCab
import sys


# Mecabを用いて、形態素解析した結果を出力する
def main(args):
    m = MeCab.Tagger("-Ochasen -d /usr/lib/mecab/dic/mecab-ipadic-neologd")
    # m = MeCab.Tagger('-Ochasen')

    text = "Pythonから形態素解析エンジンMecabを呼び出してみました。"

    print(m.parse(text))


if __name__ == "__main__":
    main(sys.argv)
