# context.area: CONSOLE
#!BPY
# -*- coding: UTF-8 -*-
# Add Location/Rotation/Scale KeyFrames
# For DDE#0050
#
# 2022.04.17 Natukikazemizoo

import bpy
import math


TARGET_OBJECT_NAME = "SpoolTank_T"
ACTION_NAME = "SpoolTank_Action"

ACTION_GROUP_NAME = "Object Transforms"
ROTATION_PATH = "rotation_euler"
KEYFRAME_TYPE = "BREAKDOWN"

HEIGHT = 0.012978
SCALE = 3
FRAME_START = 100
FRAME_END = 140


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


def clear_all_old_keyframe_points(fcurves):
    """
    Delete existing keyframe_points from F-Curves.

    Parameters
    --------------
    fcurves : bpy.types.FCurve(bpy_struct)[]
        F-Curves to remove keyframe_points.
    """
    for fcurve in fcurves:
        if fcurve.data_path == 'location' or fcurve.data_path == ROTATION_PATH \
            or fcurve.data_path == 'scale':
            clear_old_keyframe_points(fcurve)


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
    add_keyframe_point(fcurves.find(data_path, index = 1), frame, x)
    add_keyframe_point(fcurves.find(data_path, index = 2), frame, x)


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
target = bpy.data.objects[TARGET_OBJECT_NAME]
frame_current =  bpy.context.scene.frame_current

action = bpy.data.actions.get(ACTION_NAME)
if action is None:
    action =bpy.data.actions.new(ACTION_NAME)
    # Set user_fame_user to keep action data
    action.use_fake_user = True

if target.animation_data is None:
    target.animation_data_create()

if action.groups.find(ACTION_GROUP_NAME) is None: 
    bpy.context.object.animation_data.action.groups.new(ACTION_GROUP_NAME)

target.animation_data.action = action

create_fcurves(action, 'location', ACTION_GROUP_NAME)
create_fcurves(action, ROTATION_PATH, ACTION_GROUP_NAME)
create_fcurves(action, 'scale', ACTION_GROUP_NAME)

clear_all_old_keyframe_points(action.fcurves)

add_xyz_key_frame(action.fcurves, 'location', FRAME_START, 0, 0, HEIGHT)
add_xyz_key_frame(action.fcurves, 'location', FRAME_END, 0, 0, HEIGHT * SCALE)
add_xyz_key_frame(action.fcurves, ROTATION_PATH, FRAME_START, 0, 0, 0)
add_xyz_key_frame(action.fcurves, ROTATION_PATH, FRAME_END, 0, 0, math.pi * 2)
add_xyz_key_frame(action.fcurves, 'scale', FRAME_START, 1, 1, 1)
add_xyz_key_frame(action.fcurves, 'scale', FRAME_END, SCALE, SCALE, SCALE)
