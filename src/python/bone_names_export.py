#!BPY
# -*- coding: UTF-8 -*-
# Read All Bone Names
#
# 2017.09.10 Natukikazemizo

import bpy
import os
import utils_log
import utils_io_csv

# init logger
global logger
logger = utils_log.Util_Log(os.path.basename(__file__))

logger.start()

bone_names = []
header = ["name"]
bone_names.append(header)

for x in bpy.context.selected_pose_bones:
    print(x.name)
    data_row = []
    data_row.append(x.name)
    bone_names.append(data_row)

utils_io_csv.write("bone_names.csv", bone_names)

logger.end()

