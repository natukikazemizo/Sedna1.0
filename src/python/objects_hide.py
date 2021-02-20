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
 , 'Armature.N'
 , 'EyeBalls.Lens'
 , 'Armature.DDE'
 , 'Armature.Motion'
 , 'Armature.Arms.001'
 , 'Armature.Arms.002'
 , ''
 , ''
 , ''
 , ''
]

for name in objectNames:
    if name in bpy.data.objects:
        obj = bpy.data.objects[name]
        # print(obj.type)
        obj.hide_set(True)

bpy.data.collections['SubArmature'].hide_viewport = True