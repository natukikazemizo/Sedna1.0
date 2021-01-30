#!BPY
# -*- coding: UTF-8 -*-
# Judgement Utilitys
#
#
#
# 2017.08.14 Natukikazemizo
import re

def is_include_l(name):
    """judge includes .L """
    p_left = re.compile(r"(.*\.L(\.|_).*|.*\.L\Z)")
    return p_left.match(name)

