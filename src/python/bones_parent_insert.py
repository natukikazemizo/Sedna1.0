#!BPY
# -*- coding: UTF-8 -*-
# Insert Bone Parent
#
# 2017.10.28 Natukikazemizo

import bpy
import os
import utils_log

# Constants
PARENT_BONE_HEADER = "CtrlRoot_"

# init logger
global logger
logger = utils_log.Util_Log(os.path.basename(__file__))

logger.start()

amt = bpy.context.object

for x in bpy.context.selected_bones:
    if PARENT_BONE_HEADER not in x.parent.name:
        print(x.name)
        b = amt.data.edit_bones.new(PARENT_BONE_HEADER + x.name)
        b.head = x.tail
        b.tail = x.head
        b.parent = x.parent
        x.parent = b
        b.layers[28] = True
        b.layers[23] = False

logger.end()

