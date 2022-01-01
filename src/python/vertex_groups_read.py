#!BPY
# -*- coding: UTF-8 -*-
# Read Vertex Groups
#
# 2017.10.15 Natukikazemizo
#

import bpy
import os
import utils_log
import utils_io_csv
import pretty_midi
import math

# CONSTANT OF PARAMETERS
TARGET_OBJECT_NAME = "WhiteCoat.Dorothy"
OUTPUT_FILE_NAME = TARGET_OBJECT_NAME + "_Vertex_Groups"+".csv"

# init logger
global logger
logger = utils_log.Util_Log(os.path.basename(__file__))

logger.start()

group_names = []
header = ["Vertex Group Name"]
group_names.append(header)

for vertex_group in bpy.data.objects[TARGET_OBJECT_NAME].vertex_groups.items():
    print(vertex_group[0])
    data_row = []
    data_row.append(vertex_group[0])
    group_names.append(data_row)

utils_io_csv.write(OUTPUT_FILE_NAME, group_names)

logger.end()

