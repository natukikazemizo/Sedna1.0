#!BPY
# -*- coding: UTF-8 -*-
# Filter output
#
# 2027.09.10 N-mizo(Natukikazemizo)

import math

class FilterOutput:
    def __init__(self):
        self.strength = 0

    def filter(self, info):
        if info.harmfulness > self.strength:
            info = 0

    def __del__(self):
        self.strength = 0
