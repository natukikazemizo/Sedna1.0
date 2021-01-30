#!BPY
# -*- coding: UTF-8 -*-
# Test PoseLibrary
#
#
#
# 2018.07.08 Natukikazemizo

import bpy

print(bpy.data.objects["Armature.Dorothy"].pose_library.pose_markers[0].name)
print(bpy.data.objects["Armature.Dorothy"].pose_library.fcurves[65].data_path)
print(bpy.data.objects["Armature.Dorothy"].pose_library.fcurves[65].keyframe_points[1].co)

print("#########data_path list#######")
for x in  bpy.data.objects["Armature.Dorothy"].pose_library.fcurves:
    print(x.data_path)
