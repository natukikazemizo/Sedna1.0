#!BPY
# -*- coding: UTF-8 -*-
# Auto BreakDown on Piano
#
# 2017.11.05 Natukikazemizo

import bpy
import os
import utils_log

# CONSTANTS
SCENE_NAME = "Root.DorothyLoris"

TARGETS = [
    "Index_T.L",
    "Middle_T.L",
    "Ring_T.L",
    "Little_T.L",
    "Index_T.R",
    "Middle_T.R",
    "Ring_T.R",
    "Little_T.R"]

#Classes

# PARAMETER
ARMATURE_NAME = "Dorothy.Armature"

#globals
global logger

#functions
def find_data_path(bone_name_list, data_path):
    for x in bone_name_list:
        if data_path == 'pose.bones["' + x + '"].location':
            return True, x
    return False, ""

# init logger
logger = utils_log.Util_Log(os.path.basename(__file__))
bones = bpy.data.objects[ARMATURE_NAME].pose.bones
bodyModionDic = {}

logger.start()
cnt = 0
axis = ""
keyframeDic = {}
fcurveList = []
fcurve_index_dic = {}

act = bpy.data.objects[ARMATURE_NAME].animation_data.action


# flip y axis
for fcurve_index, x in enumerate(act.fcurves):
    isFind, bone_name = find_data_path(TARGETS, x.data_path)

    if isFind:
        keyframeList = []

        fcurveList.append(fcurve_index)

        cnt += 1
        if cnt == 1:
            axis = "X"
        if cnt == 2:
            axis = "Y"
        if cnt == 3:
            axis = "Z"
            cnt = 0

        if axis == "Y":
            for y in x.keyframe_points:
                y.co[1] = y.co[1] * (-1)


logger.end()

