#!BPY
# -*- coding: UTF-8 -*-
# Imaginate
#
# 2027.09.10 N-mizo(Natukikazemizo)

import math

class Imagination:
    def __init__(self):
        self.strength = 0

    def imagine(self, info):
        info = info * (self.strength + 1)

    def __del__(self):
        self.strength = 0

