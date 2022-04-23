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
        if fcurve.data_path == 'location' or fcurve.data_path == 'rotation_euler' or fcurve.data_path == 'scale':
            clear_old_breakpoints(fcurve)


def add_xyz_key_frame(fcurve, frame, x, y, z):
    if fcurve.array_index == 0:
        add_keyframe_point(fcurve, frame, x)
    elif fcurve.array_index == 1:
        add_keyframe_point(fcurve, frame, y)
    elif fcurve.array_index == 2:
        add_keyframe_point(fcurve, frame, z)


def add_location_key_frame(fcurves, frame, x, y, z):
    for fcurve in fcurves:
        if  fcurve.data_path == 'location':
            add_xyz_key_frame(fcurve, frame, x, y, z)


def add_rotation_key_frame(fcurves, frame, x, y, z):
    for fcurve in fcurves:
        if  fcurve.data_path == 'rotation_euler':
            add_xyz_key_frame(fcurve, frame, x, y, z)


def add_scale_key_frame(fcurves, frame, x, y, z):
    for fcurve in fcurves:
        if  fcurve.data_path == 'scale':
            add_xyz_key_frame(fcurve, frame, x, y, z)


def create_fcurves(action, data_path, action_group_name):
    fcurves = [fcurve for fcurve in action.fcurves if fcurve.data_path == data_path]
    if not fcurves:
        for i in range(0, 3):
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
    fcurve.keyframe_points[index].type =  "BREAKDOWN"
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
create_fcurves(action, 'rotation_euler', ACTION_GROUP_NAME)
create_fcurves(action, 'scale', ACTION_GROUP_NAME)

clear_all_old_breakpoints(action.fcurves)

height = 0.012978
scale = 3
frame_start = 100
frame_end = 140

add_location_key_frame(action.fcurves, frame_start, 0, 0, height)
add_location_key_frame(action.fcurves, frame_end, 0, 0, height * scale)
add_rotation_key_frame(action.fcurves, frame_start, 0, 0, 0)
add_rotation_key_frame(action.fcurves, frame_end, 0, math.pi, 0)
add_scale_key_frame(action.fcurves, frame_start, 1, 1, 1)
add_scale_key_frame(action.fcurves, frame_end, scale, scale, scale)

