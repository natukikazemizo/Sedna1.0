#!BPY
# -*- coding: UTF-8 -*-
# 
# Set bones Wireframe OFF
# 2019.09.22 N(natukikazemizo)

import bpy

for bone in bpy.context.object.data.bones:
    if bone.select:
        print(bone.name)
        if bone.show_wire:
            bone.show_wire = False
