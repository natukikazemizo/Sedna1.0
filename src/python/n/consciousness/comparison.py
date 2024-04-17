#!BPY
# -*- coding: UTF-8 -*-
# compare something
#
# 2027.09.10 N-mizo(Natukikazemizo)

import math

class Comparison:
    def __init__(self):
        # hoge
        self.val = 0

    def compare(self, val1, val2):
        self.val = val1 > val2

    def __del__(self):
        self.val = 0

