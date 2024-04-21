#!BPY
# -*- coding: UTF-8 -*-
# Judgment
#
# 2027.09.10 N-mizo(Natukikazemizo)

import math

class Judgment:
    def __init__(self):
        self.prejudice = 0

    def judge(self, temporary_memory):
        action = None
        return action, temporary_memory

    def __del__(self):
        self.prejudice = 0
