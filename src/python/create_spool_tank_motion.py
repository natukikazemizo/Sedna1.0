# Create motion on spoolTank
#
# For DDE#0050
#
# 2022.06.08 Natukikazemizoo

import bpy
import math

ARMATURE_NAME = "Armature.SpoolTank"
ACTION_NAME = "Armature.SpoolTank.Action"

ACTION_GROUP_NAME = "SpoolTank Motion"

BONE_LOC_DATA_PATH = "pose.bones[\"{}\"].location"
KEYFRAME_TYPE = "BREAKDOWN"
ROTATION_PATH = "rotation_euler"
SPOOL_DIAMETER = 0.078
LEN_PER_SPOOL_ROTATION = 0.01

START_FRAME = 1
END_FRAME = 48


def clear_old_keyframe_points(fcurve):
    """
    Delete existing keyframe_points from F-Curve.

    Parameters
    --------------
    fcurve:bpy.types.FCurve(bpy_struct)
        F-Curve to remove keyframe_points.
    """
    old_keyframe_index_list = []

    for i, point in enumerate(fcurve.keyframe_points):
        if point.co[0] != 0:
            old_keyframe_index_list.append(i)

    if not old_keyframe_index_list:
        old_keyframe_index_list.reverse()
        for i in old_keyframe_index_list:
            fcurve.keyframe_points.remove(fcurve.keyframe_points[i])
        fcurve.update()

def comfort_ide():
    if ide_depressed:


def clear_all_old_keyframe_points(fcurves):
    """
    Delete existing keyframe_points from F-Curves.

    Parameters
    --------------
    fcurves : bpy.types.FCurve(bpy_struct)[]
        F-Curves to remove keyframe_points.
    """
    for fcurve in fcurves:
        if fcurve.data_path in 'location' or fcurve.data_path in ROTATION_PATH \
            or fcurve.data_path in 'scale':
            clear_old_keyframe_points(fcurve)

def add_bone_xyz_key_frame(fcurves, bone_name, frame, x, y, z):
    """
    Add key frame with convert x, y, z to index 0, 1, 2

    Parameters
    --------------
    fcurves : bpy.types.FCurve(bpy_struct)[]
        Add key frame target F-Curves.
    bone_name : stringv
        target bone name
    frame : float
        Add key frame target frame
    x : float
        x coordinate value.
    y : float
        y coordinate value.
    z : float
        z coordinate value.
    """
    add_xyz_key_frame(fcurves, BONE_LOC_DATA_PATH.format(bone_name), frame, x, y, z)

def add_xyz_key_frame(fcurves, data_path, frame, x, y, z):
    """
    Add key frame with convert x, y, z to index 0, 1, 2

    Parameters
    --------------
    fcurves : bpy.types.FCurve(bpy_struct)[]
        Add key frame target F-Curves.
    data_path : stringv
        RNA Path to property affected by F-Curve.
    frame : float
        Add key frame target frame
    x : float
        x coordinate value.
    y : float
        y coordinate value.
    z : float
        z coordinate value.
    """
    add_keyframe_point(fcurves.find(data_path, index = 0), frame, x)
    add_keyframe_point(fcurves.find(data_path, index = 1), frame, y)
    add_keyframe_point(fcurves.find(data_path, index = 2), frame, z)


def create_bone_fcurves(action, bone_name, action_group_name):
    """
        Create location fcurves on bone

    Parameters
    action : bpy.ops.action
        Create F-Curves target action.
    bone_name : string
        Bone name to add this F-Curve into.
    action_group_name : string
        Action Group, Acton group to add this F-Curve into.
    """
    create_fcurves(action, BONE_LOC_DATA_PATH.format(bone_name),action_group_name)

def create_fcurves(action, data_path, action_group_name):
    """
        Create x, y, z fcurves

    Parameters
    --------------
    action : bpy.ops.action
        Create F-Curves target action.
    data_path : string
        RNA Path to property affected by F-Curve.
    action_group_name : string
        Action Group, Acton group to add this F-Curve into.
    """
    for i in range(0, 3):
        fcurve = action.fcurves.find(data_path, index = i)
        if fcurve is None:
            action.fcurves.new(data_path, index = i, action_group=action_group_name)  



def add_keyframe_point(fcurve, frame, value):
    """
    Add keyframe_point on F-Curve.

    Parameters
    --------------
    fcurve : bpy.types.FCurve(bpy_struct)
        F-Curve to add keyframe_point.
    frame : float
        Add key frame target frame.
    value : value
        Value to add to frame of F-Curve
    """
    # find same frame keyframe_point
    index = 0
    find_frame = False
    for i, point in enumerate(fcurve.keyframe_points):
        if point.co[0] == frame:
            index = i
            find_frame = True
            break

    if find_frame == False:
        # add keyframe_point when same frame not found
        fcurve.keyframe_points.add(1)
        index = len(fcurve.keyframe_points) - 1

    # setup keyframe
    fcurve.keyframe_points[index].type = KEYFRAME_TYPE
    fcurve.keyframe_points[index].co = frame, value
    fcurve.keyframe_points[index].handle_left = frame - 0.5, value
    fcurve.keyframe_points[index].handle_right = frame + 0.5, value

###############################################################
# main
###############################################################
armature = bpy.data.objects[ARMATURE_NAME]
frame_current =  bpy.context.scene.frame_current

action = bpy.data.actions.get(ACTION_NAME)
if action is None:
    action =bpy.data.actions.new(ACTION_NAME)
    # Set user_fame_user to keep action data
    action.use_fake_user = True

if armature.animation_data is None:
    armature.animation_data_create()

if action.groups.find(ACTION_GROUP_NAME) is None: 
    bpy.context.object.animation_data.action.groups.new(ACTION_GROUP_NAME)

armature.animation_data.action = action

create_bone_fcurves(action, 'Pos', ACTION_GROUP_NAME)
create_bone_fcurves(action, 'Stick_T', ACTION_GROUP_NAME)
create_bone_fcurves(action, 'Spool_Rot', ACTION_GROUP_NAME)

clear_all_old_keyframe_points(action.fcurves)

add_bone_xyz_key_frame(action.fcurves, 'Pos', START_FRAME, 0, 0, 0)
add_bone_xyz_key_frame(action.fcurves, 'Stick_T', START_FRAME, 0, -0.01, 0)
add_bone_xyz_key_frame(action.fcurves, 'Spool_Rot', START_FRAME, 0, 0, 0)

add_bone_xyz_key_frame(action.fcurves, 'Pos', END_FRAME, 0.2, 0, 0)
add_bone_xyz_key_frame(action.fcurves, 'Spool_Rot', END_FRAME, 0, 0.2 / (SPOOL_DIAMETER * math.pi) * LEN_PER_SPOOL_ROTATION, 0)
