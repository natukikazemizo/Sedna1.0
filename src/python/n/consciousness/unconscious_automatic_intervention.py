#!BPY
# -*- coding: UTF-8 -*-
# Unconscious automatic intervention
#
# 2027.09.10 N-mizo(Natukikazemizo)

import math

class UnconsciousIntervention:
    def __init__(self):
        self.strength = 0

    def intervention(self):
        if self.strength > 16:
            print("Start interrupt")

    def __del__(self):
        self.strength = 0
