#!BPY
# -*- coding: UTF-8 -*-
# Add Path to Custom Shape
#
# 2023.05.05 Natukikazemizo

import bpy

CTRL_PIC_PATH = "//..\\..\\CtrlPic.blend"

print("*** START ***")
for obj in bpy.data.objects:
    if obj.type == "ARMATURE":
        print("--------")
        print(obj.name)
        print("--------")
        for bone in obj.pose.bones:
            if bone.custom_shape != None:
                print(bone.name + ": " + bone.custom_shape.name)
                bone.custom_shape = bpy.data.objects[bone.custom_shape.name, CTRL_PIC_PATH]
print("*** END ***")
     



 