#!BPY
# -*- coding: UTF-8 -*-
# Input
#
# 2027.09.10 N-mizo(Natukikazemizo)

import math

class Input:
    def __init__(self):
        self.vessel = {}

    def input(self, key, info):
        self.vessel[key] = info

    def __del__(self):
        self.vessel = {}
