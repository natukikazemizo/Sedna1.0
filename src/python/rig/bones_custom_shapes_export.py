#!BPY
# -*- coding: UTF-8 -*-
# Export Custome Shape Settings
#
# 2017.09.10 Natukikazemizo

import bpy
import os
import utils_log
import utils_io_csv

# Constants
WORK_FILE_NAME = "custom_shape_settings.csv"

# init logger
global logger
logger = utils_log.Util_Log(os.path.basename(__file__))

logger.start()

bone_names = []
header = ["bone_name", "custom_shape", "custom_shape_scale"]
bone_names.append(header)

for x in bpy.context.selected_pose_bones:
    if x.custom_shape != None:
        print(x.name)
        data_row = []
        data_row.append(x.name)
        data_row.append(x.custom_shape.name)
        data_row.append(x.custom_shape_scale)
        bone_names.append(data_row)

utils_io_csv.write(WORK_FILE_NAME, bone_names)

logger.end()

