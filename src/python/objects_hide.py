#!BPY
# -*- coding: UTF-8 -*-
# Hide not use Objects
#
# 2021.02.01 by N(natukikazemizo)

import bpy

objectNames = [
   'Curve.N'
 , 'Armature.Pillow_DDE'
 , 'Armature.Pillow_N'
 , 'Armature.Blanket'
 , 'Armature.Clock'
 , 'Armature.Andon'
 , 'hoge'
]

for name in objectNames:
    if name 
    bpy.data.objects[name].hide_viewport = True
