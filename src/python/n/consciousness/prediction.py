#!BPY
# -*- coding: UTF-8 -*-
# Prediction
#
# 2027.09.10 N-mizo(Natukikazemizo)

import math

class Prediction:
    def __init__(self):
        # hoge
        self.accuracy = 0.5

    def prediction(self, premise):
        return premise * self.accuracy

    def __del__(self):
        self.accuracy = 0.5
