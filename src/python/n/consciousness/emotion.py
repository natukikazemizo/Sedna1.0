#!BPY
# -*- coding: UTF-8 -*-
# Cause emotions
#
# 2027.09.10 N-mizo(Natukikazemizo)

import math

class Emotion:
    def __init__(self):
        self.state = (0, 0, 0)
        self.range = 0

    def emote(self, temporary_memory):
        self.range += 0.1
        return temporary_memory

    def __del__(self):
        self.state = (0, 0, 0)
        self.range = 0
