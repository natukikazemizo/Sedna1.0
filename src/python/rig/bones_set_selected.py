#!BPY
# -*- coding: UTF-8 -*-
# Set Up Selected Bones
#
# 2017.10.19 Natukikazemizo

import bpy
import os
import utils_log


# init logger
global logger
logger = utils_log.Util_Log(os.path.basename(__file__))

logger.start()

for x in bpy.context.selected_pose_bones:
    if x.custom_shape != None:
        print(x.name)
        x.ik_stretch = 0.1

logger.end()

