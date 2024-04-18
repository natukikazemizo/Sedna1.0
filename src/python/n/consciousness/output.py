#!BPY
# -*- coding: UTF-8 -*-
# Output
#
# 2027.09.10 N-mizo(Natukikazemizo)

import math

class Output:
    def __init__(self):
        self.fatigue = 0

    def output(self):
        self.fatigue += 1

    def __del__(self):
        self.fatigue = 0
