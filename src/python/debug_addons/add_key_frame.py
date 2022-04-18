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
F_CURVE_X_LOCATION = 0
F_CURVE_Y_LOCATION = 1
F_CURVE_Z_LOCATION = 2
F_CURVE_X_ROTATION = 3
F_CURVE_Y_ROTATION = 4
F_CURVE_Z_ROTATION = 5
F_CURVE_X_SCALE = 6
F_CURVE_Y_SCALE = 7
F_CURVE_Z_SCALE = 8

ACTION_GROUP_NAME = "Object Transforms"


def clear_old_breakpoints(fcurve):
    old_keyframe_index_list = []

    for i, point in enumerate(fcurve.keyframe_points):
        if point.co[0] != 0:
            old_keyframe_index_list.append(i)

    if len(old_keyframe_index_list) > 0:
        old_keyframe_index_list.reverse()
        for i in old_keyframe_index_list:
            fcurve.keyframe_points.remove(fcurve.keyframe_points[i])
        fcurve.update()


def clear_all_old_breakpoints(fcurves):
    clear_old_breakpoints(fcurves[F_CURVE_X_LOCATION])
    clear_old_breakpoints(fcurves[F_CURVE_Y_LOCATION])
    clear_old_breakpoints(fcurves[F_CURVE_Z_LOCATION])
    clear_old_breakpoints(fcurves[F_CURVE_X_ROTATION])
    clear_old_breakpoints(fcurves[F_CURVE_Y_ROTATION])
    clear_old_breakpoints(fcurves[F_CURVE_Z_ROTATION])
    clear_old_breakpoints(fcurves[F_CURVE_X_SCALE])
    clear_old_breakpoints(fcurves[F_CURVE_X_SCALE])
    clear_old_breakpoints(fcurves[F_CURVE_X_SCALE])


def add_location_key_frame(fcurves, frame, x, y, z):
    add_keyframe_point(fcurves[F_CURVE_X_LOCATION], frame, x)
    add_keyframe_point(fcurves[F_CURVE_Y_LOCATION], frame, y)
    add_keyframe_point(fcurves[F_CURVE_Z_LOCATION], frame, z)


def add_rotation_key_frame(fcurves, frame, x, y, z):
    add_keyframe_point(fcurves[F_CURVE_X_ROTATION], frame, x)
    add_keyframe_point(fcurves[F_CURVE_Y_ROTATION], frame, y)
    add_keyframe_point(fcurves[F_CURVE_Z_ROTATION], frame, z)


def add_scale_key_frame(fcurves, frame, x, y, z):
    add_keyframe_point(fcurves[F_CURVE_X_SCALE], frame, x)
    add_keyframe_point(fcurves[F_CURVE_Y_SCALE], frame, y)
    add_keyframe_point(fcurves[F_CURVE_Z_SCALE], frame, z)


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

if action.fcurves is None or len(action.fcurves) == 0:
    action.fcurves.new('location', action_group=ACTION_GROUP_NAME)
    action.fcurves.new('location', index=1, action_group=ACTION_GROUP_NAME)
    action.fcurves.new('location', index=2, action_group=ACTION_GROUP_NAME)
    action.fcurves.new('rotation_euler', action_group=ACTION_GROUP_NAME)
    action.fcurves.new('rotation_euler', index=1, action_group=ACTION_GROUP_NAME)
    action.fcurves.new('rotation_euler', index=2, action_group=ACTION_GROUP_NAME)    
    action.fcurves.new('scale', action_group=ACTION_GROUP_NAME)
    action.fcurves.new('scale', index=1, action_group=ACTION_GROUP_NAME)
    action.fcurves.new('scale', index=2, action_group=ACTION_GROUP_NAME)

clear_all_old_breakpoints(action.fcurves)

add_location_key_frame(action.fcurves, 10, 0, 0, 0)
add_location_key_frame(action.fcurves, 12, 0.2, 0.3, 0.1)
add_rotation_key_frame(action.fcurves, 10, 0, 0, 0)
add_rotation_key_frame(action.fcurves, 12, math.pi / 6, 0, 0)
add_scale_key_frame(action.fcurves, 10, 1, 1, 1)
add_scale_key_frame(action.fcurves, 12, 3, 4, 5)

