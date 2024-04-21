#!BPY
# -*- coding: UTF-8 -*-
# Input
#
# 2027.09.10 N-mizo(Natukikazemizo)



class Input:
    def __init__(self):
        self.temporary_memory = {}

    def input(self, info):
        return self.temporary_memory

    def __del__(self):
        self.temporary_memory = {}
