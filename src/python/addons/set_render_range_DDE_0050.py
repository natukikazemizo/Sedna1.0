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
import re

__author__ = "N mizo <https://x.com/natukikazemizo>"
__status__ = "In Feature Review"
__version__ = "0.1"
__date__ = "10 August 2024"

bl_info = {
    "name" : "DDE#0050 Special functions",
    "author" : "N mizo",
    "version" : (0, 1),
    "blender" : (4, 1, 1),
    "location" : "3D View > UI > Render Range",
    "description" : "Special functions for DDE#0050",
    "warning" : "",
    "wiki_url" : "",
    "tracker_url" : "",
    "category" : "3D View"
}


def set_frame_range(self, frame_start, frame_end):
    bpy.context.scene.frame_start = frame_start
    bpy.context.scene.frame_end = frame_end
    bpy.context.scene.frame_current = frame_start

def hide_object(self, object_name, hide_set):
    if bpy.data.objects[object_name].visible_get() or not hide_set:
        bpy.data.objects[object_name].hide_set(hide_set)

class Render_range_Panel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'DDE_0050'
    bl_label = 'DDE_0050'

    def draw(self, context):
        layout = self.layout
        column = layout.column(align=False)

        scene = context.scene
        column.label(text="Select scene")
        # Add PullDown
        # プルダウン表示
        column.prop(scene, "scene_no_enum", text="No")
        column.operator('set.range')

        column.separator()

        column.label(text="Show/Hide Objects")
        # Add Check Box
        # チェックボックス表示
        column.prop(scene, "hide_Studio_bool", text="Studio")
        column.prop(scene, "hide_DDE_Armature_bool", text="DDE Armature")
        column.prop(scene, "hide_N_Armature_bool", text="N Armature")
        column.operator('set.hideshow')

        column.separator()
        column.label(text="Hide Select Hair Line")
        column.prop(scene, "hide_select_hair_line_bool", text="hide_select")
        column.operator('set.hairline_hideselect')

        column.separator()
        column.label(text="Move Hair Bones to Bone Collections")
        column.operator('set.hairbone_bonecollections')

class Set_Range_btn(bpy.types.Operator):
    bl_idname = 'set.range'
    bl_label = 'Set Range'
    bl_description = 'Set frame range.'

    def execute(self,context):
        scene = context.scene
        if scene.scene_no_enum == "ITEM_1":
            set_frame_range(self, 400, 962)
        elif scene.scene_no_enum == "ITEM_2":
            set_frame_range(self, 1200, 1745)
        elif scene.scene_no_enum == "ITEM_3":
            set_frame_range(self, 2000, 2480)
        elif scene.scene_no_enum == "ITEM_4":
            set_frame_range(self, 2800, 3821)
        elif scene.scene_no_enum == "ITEM_5":
            set_frame_range(self, 4200, 4990)
        elif scene.scene_no_enum == "ITEM_6":
            set_frame_range(self, 5300, 6460)

        return {'FINISHED'}

class Set_HideShow_btn(bpy.types.Operator):
    bl_idname = 'set.hideshow'
    bl_label = 'Show'
    bl_description = 'Set Show cheked Armature & Hide not checked Armature'



    def execute(self,context):
        scene = context.scene
        
        hide_object(self, "Camera.Main", not scene.hide_Studio_bool)
        hide_object(self, "Armature.Studio", not scene.hide_Studio_bool)
        hide_object(self, "Armature.DDE", not scene.hide_DDE_Armature_bool)
        hide_object(self, "Armature.N", not scene.hide_N_Armature_bool)

        return {'FINISHED'}





class Set_HairLine_HideSelect_btn(bpy.types.Operator):
    bl_idname = 'set.hairline_hideselect'
    bl_label = 'Set hide_select'
    bl_description = 'Set hide_select True/False to Hair Line Bones.'

    def execute(self,context):
        scene = context.scene
        pattern='.*Hair.*Line.*'
        is_hair_line=re.compile(pattern)

        for bone in bpy.data.objects["Armature.DDE"].data.bones:
            if is_hair_line.match(bone.name):
                bone.hide_select = scene.hide_select_hair_line_bool

        return {'FINISHED'}


class Set_HairBone_BoneCollections_btn(bpy.types.Operator):
    bl_idname = 'set.hairbone_bonecollections'
    bl_label = 'Set Bone Collections'
    bl_description = 'Move Hair bones to appropriate Bone Collections'

    def execute(self,context):

        ptn_hair_ctrl ='.*Hair.*(Line|_T).*'
        ptn_hair_bone ='^(?!.*Hair.*(Line|_T).*|Hair).*Hair.*'

        is_hair_ctrl=re.compile(ptn_hair_ctrl)
        is_hair_bone=re.compile(ptn_hair_bone)

        collections_all = bpy.data.objects['Armature.DDE'].data.collections_all

        for bone in bpy.data.objects["Armature.DDE"].data.bones:
            if is_hair_ctrl.match(bone.name):
                collections_all["All_Ctrls"].assign(bone)
                collections_all["Ctrl.Hair.All"].assign(bone)
                collections_all["All_Bones"].unassign(bone)
                collections_all["Bones.Hair"].unassign(bone)

            elif is_hair_bone.match(bone.name):
                collections_all["All_Ctrls"].unassign(bone)
                collections_all["Ctrl.Hair.All"].unassign(bone)
                collections_all["All_Bones"].assign(bone)
                collections_all["Bones.Hair"].assign(bone)

        return {'FINISHED'}


# Initializing properties
# プロパティ初期化
def init_props():
    scene = bpy.types.Scene
    scene.scene_no_enum = bpy.props.EnumProperty(
        name="Scene No.",
        description="Scene No.(enum)",
        items=[
            ('ITEM_1', "scene_01", "Scene 01"),
            ('ITEM_2', "scene_02", "Scene 02"),
            ('ITEM_3', "scene_03", "Scene 03"),
            ('ITEM_4', "scene_04", "Scene 04"),
            ('ITEM_5', "scene_05", "Scene 05"),
            ('ITEM_6', "scene_06", "Scene 06")
        ],
        default='ITEM_1'
    )
    scene.hide_Studio_bool = bpy.props.BoolProperty(
        name="Hide Studio",
        description="Hide Studio(bool)",
        default=False
    )
    scene.hide_DDE_Armature_bool = bpy.props.BoolProperty(
        name="Hide DDE Armature",
        description="Hide DDE Armature(bool)",
        default=False
    )
    scene.hide_N_Armature_bool = bpy.props.BoolProperty(
        name="Hide N Armature",
        description="Hide N Armature(bool)",
        default=False
    )
    scene.hide_select_hair_line_bool = bpy.props.BoolProperty(
        name="hide_selecct Hair Line",
        description="hide_select of Hair Line Bones",
        default=True
    )


# Delete Property
# プロパティ削除
def clear_props():
    scene = bpy.types.Scene
    del scene.scene_no_enum
    del scene.hide_Studio_bool
    del scene.hide_DDE_Armature_bool
    del scene.hide_N_Armature_bool
    del scene.hide_select_hair_line_bool


def register():
    init_props()
    bpy.utils.register_class(Render_range_Panel)
    bpy.utils.register_class(Set_Range_btn)
    bpy.utils.register_class(Set_HideShow_btn)
    bpy.utils.register_class(Set_HairLine_HideSelect_btn)
    bpy.utils.register_class(Set_HairBone_BoneCollections_btn)


def unregister():
    clear_props()
    bpy.utils.unregister_class(Render_range_Panel)
    bpy.utils.unregister_class(Set_Range_btn)
    bpy.utils.unregister_class(Set_HideShow_btn)
    bpy.utils.unregister_class(Set_HairLine_HideSelect_btn)
    bpy.utils.unregister_class(Set_HairBone_BoneCollections_btn)



if __name__ == "__main__":
    register()


