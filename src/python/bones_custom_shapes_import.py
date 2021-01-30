#!BPY
# -*- coding: UTF-8 -*-
# Clone Custome Shape 
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

header, data = utils_io_csv.read(WORK_FILE_NAME)

for row in data:
    if bpy.context.object.pose.bones.find(row[0]) == -1:
        logger.warn("Bone not found. Bone name is " + row[0])
        break
    if bpy.data.objects.find(row[1]) == -1:
        logger.warn("Object not found. Object name is " + row[1])
        break
    bone = bpy.context.object.pose.bones[row[0]]
    print(bone.name)
    bone.custom_shape = None
    bone.custom_shape = bpy.data.objects[row[1]]
    bone.custom_shape_scale = float(row[2])

logger.end()

