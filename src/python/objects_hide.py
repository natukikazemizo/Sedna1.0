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
 , 'Lens'
 , 'Armature.DDE'
 , 'Armature.Motion'
 , 'Armature.Arms.001'
 , 'Armature.Arms.002'
 , 'Armature.Blanket_proxy'
 , 'Armature.Clock_proxy'
 , ''
 , ''
]

# hide objects
for name in objectNames:
    if name in bpy.context.scene.view_layers[0].objects:
        obj = bpy.context.scene.view_layers[0].objects[name]
        # print(obj.type)
        obj.hide_set(True)

# hide Collections
bpy.data.collections['SubArmature'].hide_viewport = True