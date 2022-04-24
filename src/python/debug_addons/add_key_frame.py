# context.area: CONSOLE
#!BPY
# -*- coding: UTF-8 -*-
# Add Location/Rotation/Scale KeyFrames
# For DDE#0040
#
# 2022.04.17 Natukikazemizoo

import bpy
import math


TARGET_OBJECT_NAME = "SpoolTank_T"
ACTION_NAME = "SpoolTank_Action"

ACTION_GROUP_NAME = "Object Transforms"
ROTATION_PATH = "rotation_euler"
KEYFRAME_TYPE = "BREAKDOWN"


def clear_old_breakpoints(fcurve):
    old_keyframe_index_list = []

    for i, point in enumerate(fcurve.keyframe_points):
        if point.co[0] != 0:
            old_keyframe_index_list.append(i)

    if not old_keyframe_index_list:
        old_keyframe_index_list.reverse()
        for i in old_keyframe_index_list:
            fcurve.keyframe_points.remove(fcurve.keyframe_points[i])
        fcurve.update()


def clear_all_old_breakpoints(fcurves):
    for fcurve in fcurves:
        if fcurve.data_path == 'location' or fcurve.data_path == ROTATION_PATH \
            or fcurve.data_path == 'scale':
            clear_old_breakpoints(fcurve)


def add_xyz_key_frame(fcurves, data_path, frame, x, y, z):
    add_keyframe_point(fcurves.find(data_path, index = 0), frame, x)
    add_keyframe_point(fcurves.find(data_path, index = 1), frame, y)
    add_keyframe_point(fcurves.find(data_path, index = 2), frame, z)


def create_fcurves(action, data_path, action_group_name):
    for i in range(0, 3):
        fcurve = action.fcurves.find(data_path, index = i)
        if fcurve is None:
            action.fcurves.new(data_path, index = i, action_group=action_group_name)  


def add_keyframe_point(fcurve, frame, value):

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

clear_all_old_breakpoints(action.fcurves)

height = 0.012978
scale = 3
frame_start = 100
frame_end = 140

add_xyz_key_frame(action.fcurves, 'location', frame_start, 0, 0, height)
add_xyz_key_frame(action.fcurves, 'location', frame_end, 0, 0, height * scale)
add_xyz_key_frame(action.fcurves, ROTATION_PATH, frame_start, 0, 0, 0)
add_xyz_key_frame(action.fcurves, ROTATION_PATH, frame_end, 0, math.pi, 0)
add_xyz_key_frame(action.fcurves, 'scale', frame_start, 1, 1, 1)
add_xyz_key_frame(action.fcurves, 'scale', frame_end, scale, scale, scale)

