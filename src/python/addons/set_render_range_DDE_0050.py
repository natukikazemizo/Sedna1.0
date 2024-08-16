# <pep8-80 compliant>

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy

__author__ = "N mizo <https://x.com/natukikazemizo>"
__status__ = "In Feature Review"
__version__ = "0.1"
__date__ = "10 August 2024"

bl_info = {
    "name" : "Set render Range",
    "author" : "N mizo",
    "version" : (0, 1),
    "blender" : (4, 1, 1),
    "location" : "3D View > UI > Render Range",
    "description" : "Specifying a hard-coded render range per scene.",
    "warning" : "",
    "wiki_url" : "",
    "tracker_url" : "",
    "category" : "3D View"
}

def toggle_hide(self, object_name):
    obj = bpy.data.objects[object_name]
    if obj.hide_get():
        obj.hide_set(False)
    else:
        obj.hide_set(True)


def set_frame_range(self, frame_start, frame_end):
    bpy.context.scene.frame_start = frame_start
    bpy.context.scene.frame_end = frame_end


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
        column.operator('range.07')
        column.operator('range.08')

class Scene_01_btn(bpy.types.Operator):
    bl_idname = 'range.scene_01'
    bl_label = 'scene_01'
    bl_description = 'scene_01'
   
   
    def execute(self,context):
        # 010_Check the dinner menu
        set_frame_range(self, 400, 962)
   
        return {'FINISHED'}

class Scene_02_btn(bpy.types.Operator):
   bl_idname = 'range.scene_02'
   bl_label = 'scene_02'
   bl_description = 'scene_02'
   
   def execute(self,context):
        # 020_Connect N
        set_frame_range(self, 1200, 1745)
   
        return {'FINISHED'}

class Scene_03_btn(bpy.types.Operator):
   bl_idname = 'range.scene_03'
   bl_label = 'scene_03'
   bl_description = 'scene_03'
   
   def execute(self,context):
        # 030_debugging N
        set_frame_range(self, 2000, 2480)
   
        return {'FINISHED'}

class Scene_04_btn(bpy.types.Operator):
   bl_idname = 'range.scene_04'
   bl_label = 'scene_04'
   bl_description = 'scene_04'
   
   def execute(self,context):
        # 040_N's memory tampering
        set_frame_range(self, 2800, 3821)
   
        return {'FINISHED'}

class Scene_05_btn(bpy.types.Operator):
   bl_idname = 'range.scene_05'
   bl_label = 'scene_05'
   bl_description = 'scene_05'
   
   def execute(self,context):
        # 050_DDE penetrates the kernel
        set_frame_range(self, 4200, 4990)
   
        return {'FINISHED'}

class Scene_06_btn(bpy.types.Operator):
    bl_idname = 'range.scene_06'
    bl_label = 'scene_06'
    bl_description = 'scene_06'
   
    def execute(self,context):
        # 060_N appears
        set_frame_range(self, 5300, 6460)
   
        return {'FINISHED'}

class Toggle_DDE_armature_btn(bpy.types.Operator):
    bl_idname = 'range.07'
    bl_label = 'tgl DDE Amt'
    bl_description = 'Show/Hide Armature.DDE'

    def execute(self,context):
        toggle_hide(self, "Armature.DDE")

        return {'FINISHED'}

class Toggle_N_armature_btn(bpy.types.Operator):
    bl_idname = 'range.08'
    bl_label = 'tgl N Amt'
    bl_description = 'Show/Hide Armature.N'

    def execute(self,context):
        toggle_hide(self, "Armature.N")

        return {'FINISHED'}


def register():
    bpy.utils.register_class(Render_range_Panel)
    bpy.utils.register_class(Scene_01_btn)
    bpy.utils.register_class(Scene_02_btn)
    bpy.utils.register_class(Scene_03_btn)
    bpy.utils.register_class(Scene_04_btn)
    bpy.utils.register_class(Scene_05_btn)
    bpy.utils.register_class(Scene_06_btn)
    bpy.utils.register_class(Toggle_DDE_armature_btn)
    bpy.utils.register_class(Toggle_N_armature_btn)

def unregister():
    bpy.utils.unregister_class(Scene_01_btn)
    bpy.utils.unregister_class(Scene_02_btn)
    bpy.utils.unregister_class(Scene_03_btn)
    bpy.utils.unregister_class(Scene_04_btn)
    bpy.utils.unregister_class(Scene_05_btn)
    bpy.utils.unregister_class(Scene_06_btn)
    bpy.utils.unregister_class(Toggle_DDE_armature_btn)
    bpy.utils.unregister_class(Toggle_N_armature_btn)
    bpy.utils.unregister_class(Render_range_Panel)



if __name__ == "__main__":
    register()


