# !BPY
# -*- coding: UTF-8 -*-
# Render
#
# Add Change Render Range Button
#
# 2024.08.10 N mizo (natukikazemizo)
#

import bpy
  
class Render_range_Panel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Render Range'
    bl_label = 'Select render range'
    
    def draw(self, context):
        layout = self.layout
        column = layout.column(align=False)
        column.operator('range.scene_01')
        column.operator('range.scene_02')
        column.operator('range.scene_03')
        column.operator('range.scene_04')
        column.operator('range.scene_05')
        column.operator('range.scene_06')

class Scene_01_btn(bpy.types.Operator):
    bl_idname = 'range.scene_01'
    bl_label = 'scene_01'
    bl_description = 'scene_01'
   
   
    def execute(self,context):
        # 010_Check the dinner menu
        bpy.context.scene.frame_start = 400
        bpy.context.scene.frame_end = 962
   
        return {'FINISHED'}

class Scene_02_btn(bpy.types.Operator):
   bl_idname = 'range.scene_02'
   bl_label = 'scene_02'
   bl_description = 'scene_02'
   
   def execute(self,context):
        # 020_Connect N
        bpy.context.scene.frame_start = 1200
        bpy.context.scene.frame_end = 1745
   
        return {'FINISHED'}

class Scene_03_btn(bpy.types.Operator):
   bl_idname = 'range.scene_03'
   bl_label = 'scene_03'
   bl_description = 'scene_03'
   
   def execute(self,context):
        # 030_debugging N
        bpy.context.scene.frame_start = 2000
        bpy.context.scene.frame_end = 2480
   
        return {'FINISHED'}

class Scene_04_btn(bpy.types.Operator):
   bl_idname = 'range.scene_04'
   bl_label = 'scene_04'
   bl_description = 'scene_04'
   
   def execute(self,context):
        # 040_N's memory tampering
        bpy.context.scene.frame_start = 2800
        bpy.context.scene.frame_end = 3821
   
        return {'FINISHED'}

class Scene_05_btn(bpy.types.Operator):
   bl_idname = 'range.scene_05'
   bl_label = 'scene_05'
   bl_description = 'scene_05'
   
   def execute(self,context):
        # 050_DDE penetrates the kernel
        bpy.context.scene.frame_start = 4200
        bpy.context.scene.frame_end = 4990
   
        return {'FINISHED'}

class Scene_06_btn(bpy.types.Operator):
   bl_idname = 'range.scene_06'
   bl_label = 'scene_06'
   bl_description = 'scene_06'
   
   def execute(self,context):
        # 060_N appears
        bpy.context.scene.frame_start = 5300
        bpy.context.scene.frame_end = 6460
   
        return {'FINISHED'}


bpy.utils.register_class(Render_range_Panel)
bpy.utils.register_class(Scene_01_btn)
bpy.utils.register_class(Scene_02_btn)
bpy.utils.register_class(Scene_03_btn)
bpy.utils.register_class(Scene_04_btn)
bpy.utils.register_class(Scene_05_btn)
bpy.utils.register_class(Scene_06_btn)
