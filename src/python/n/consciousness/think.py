#!BPY
# -*- coding: UTF-8 -*-
# Think
#
# 2027.09.10 N-mizo(Natukikazemizo)

import math

class Think:
    def __init__(self):
        self.concentration = 128

    def think(self):
        self.concentration -= 1

    def __del__(self):
        self.concentration = 128
