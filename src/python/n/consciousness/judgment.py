#!BPY
# -*- coding: UTF-8 -*-
# Judgment
#
# 2027.09.10 N-mizo(Natukikazemizo)

import math

class Judgment:
    def __init__(self):
        self.prejudice = 0

    def judge(self, value1, value2):
        return value1 > (value2 + self.prejudice)

    def __del__(self):
        self.prejudice = 0
