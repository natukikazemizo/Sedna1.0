#!BPY
# -*- coding: UTF-8 -*-
# Think
#
# 2027.09.10 N-mizo(Natukikazemizo)

import math

class Think:
    def __init__(self, concentration, delta):
        self.concentration = concentration

    def think(self, trigger):
        while self.concentration > 0:
            # Thinking consumes concentration.
            self.concentration -= self.delta
        

    def __del__(self):
        # freedom from thinking
        self.concentration = 0
