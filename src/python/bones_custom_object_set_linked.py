#!BPY
# -*- coding: UTF-8 -*-
# Change bone's cutom object to linked object
# ボーンのカスタムオブジェクトをリンクされたオブジェクトに変更する
#
# 2025.03.27 Natukikazemizo 作成途中で放置

import bpy

# アクティブなオブジェクトがアーマチュアであることを確認
obj = bpy.context.active_object
if obj and obj.type == 'ARMATURE':
    armature = obj.data
    
    # ポーズモードのボーンをチェック
    for bone in armature.bones:
        # 対応するポーズボーンを取得
        pose_bone = obj.pose.bones.get(bone.name)
        if pose_bone:
            # カスタムシェイプが設定されているか確認
            if pose_bone.custom_shape:
                print(f"ボーン '{bone.name}' にカスタムシェイプが設定されています: {pose_bone.custom_shape.name}")
            else:
                print(f"ボーン '{bone.name}' にカスタムシェイプは設定されていません")
else:
    print("アクティブなオブジェクトがアーマチュアではありません")


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

