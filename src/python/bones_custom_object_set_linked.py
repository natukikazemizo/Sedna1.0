#!BPY
# -*- coding: UTF-8 -*-
# Change bone's cutom object to linked object
# ボーンのカスタムオブジェクトをリンクされたオブジェクトに変更する
#
# 2025.03.29 Nミゾ(Natukikazemizo) アイデアが思いついたので、作成

import bpy
import sys

# .blend file name for storing custom_shape
# custom_shape 格納用 .blendファイル名
CUSTOM_SHAPES_BLEND = 'CtrlPic.blend'


print('######## START ########')

if bpy.data.libraries[CUSTOM_SHAPES_BLEND]:
    for obj in bpy.data.objects:
        if obj and obj.type == 'ARMATURE':
            print('Check Armature:' + obj.name)
            
            for bone in obj.data.bones:
                # Get pose bone
                pose_bone = obj.pose.bones.get(bone.name)
                if pose_bone:
                    if pose_bone.custom_shape:
                        if not pose_bone.custom_shape.library:
                            print(f"Bone '{bone.name}' " \
                                "custom shape: {pose_bone.custom_shape.name} "\
                                    "without library")
else:
    print('The .blend file containing custom_shape is not linked.')
    print('custom_shape 格納用 .blendファイル がリンクされていません。')

print('########  END  ########')


## プロンプトで実験結果

# >>> bpy.data.objects["CtrlPic.Rot"].data.library
# bpy.data.libraries['CtrlPic.blend']

# >>> bpy.data.objects["CtrlPic.Rot"].library
# bpy.data.libraries['CtrlPic.blend']

# >>> bpy.data.objects["Object_T"].library
# >>> bpy.data.objects["Object_T"].data.library
# Traceback (most recent call last):
#   File "<blender_console>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'library'

# >>> bpy.data.objects["Object_T"].data
# >>> bpy.data.objects["Object_T"].data.library
# Traceback (most recent call last):
#   File "<blender_console>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'library'

