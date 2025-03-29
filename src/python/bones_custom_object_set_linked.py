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

# Collection name for storing custom_shape
# custom_shape 格納用 Collection名
CUSTOM_SHAPES_COLLECTION = 'CtrlPic'


def set_linked_custom_shape(self, pose_bone):
    """
    Parameters
    ----------
    pose_bone : bpy_struct
        PoseBone to replace custom shape<br>
        Custom shape を置換する Pose Bone
    """
    if pose_bone.custom_shape.name not in \
        bpy.data.collections[CUSTOM_SHAPES_COLLECTION].objects:
        print ("custom shape: {pose_bone.custom_shape.name} "\
                "not in Linked CtrlPic Collection library")
        return
    pose_bone.custom_shape = bpy.data.collections[CUSTOM_SHAPES_COLLECTION].objects[pose_bone.name]
    print(f"bone '{pose_bone.name}' custom shape: '{pose_bone.custom_shape.name}' fixed to linked object")


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
                                "custom shape: '{pose_bone.custom_shape.name}' "\
                                    "without library")
else:
    print('The .blend file containing custom_shape is not linked.')
    print('custom_shape 格納用 .blendファイル がリンクされていません。')

print('########  END  ########')


