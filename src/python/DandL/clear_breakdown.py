#!BPY
# -*- coding: UTF-8 -*-
# Clear BreakDown KeyFrames
#
# 2017.10.29 Natukikazemizo

import bpy
import os
import utils_log

# CONSTANTS
SCENE_NAME = "Root.DorothyLoris"

# Articulation Dictionary

START_FRAME = 3048
FRAME_PAR_MEASURE = 48
MEASURE = 2

#Classes

# PARAMETER
ARMATURE_NAMES = ["Dorothy.Armature", "Loris.Armature"]

#globals
global logger

#functions

# init logger
logger = utils_log.Util_Log(os.path.basename(__file__))

logger.start()

for armature_name in ARMATURE_NAMES:

    act = bpy.data.objects[armature_name].animation_data.action

    # delete all old breakdowns and create fcurve_index_dictionary
    for fcurve_index, x in enumerate(act.fcurves):
        oldBreakdownList = []

        for i, y in enumerate(x.keyframe_points):
            if y.type == "BREAKDOWN":
                oldBreakdownList.append(i)

        if len(oldBreakdownList) > 0:
            oldBreakdownList.reverse()
            for y in oldBreakdownList:
                x.keyframe_points.remove(x.keyframe_points[y])
            x.update()

logger.end()

