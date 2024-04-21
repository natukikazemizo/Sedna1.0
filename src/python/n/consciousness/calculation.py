#!BPY
# -*- coding: UTF-8 -*-
# Calculation
#
# 2027.09.10 N-mizo(Natukikazemizo)

import math

class Calculation:
    def __init__(self):
        self.num = 0

    def add(self, val):
        self.num += val

    def calculate(self, temporary_memory):
        return temporary_memory

    def __del__(self):
        self.num = 0
