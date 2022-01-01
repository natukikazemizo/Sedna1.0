#!BPY
# -*- coding: UTF-8 -*-
# Convert Utilitys
#
#
#
# 2017.08.14 Natukikazemizo
import re

def cnv_l_2_r(name_l):
    """convert Name .L to .R """
    name_r = re.sub(r"\.L\.", ".R.", name_l)
    name_r = re.sub(r"\.L_", ".R_", name_r)
    name_r = re.sub(r"\.L\Z", ".R", name_r)
    return name_r


