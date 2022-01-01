#!BPY
# -*- coding: UTF-8 -*-
# Create Piano Armature Settings
#
# 2017.10.03 Natukikazemizo
#

import bpy
import os
import utils_log
import utils_io_csv
import math

# init logger
global logger
logger = utils_log.Util_Log(os.path.basename(__file__))

logger.start()

for x in bpy.context.selected_pose_bones:
    print(x.name)
    
    # SET UP IK CONSTRAINT
    if x.constraints.find("IK") == -1:
        newConstraint = x.constraints.new(type="IK")
        newConstraint.name = "IK"
    constraint = x.constraints["IK"]
    constraint.target = bpy.data.objects["Piano_Armature"]
    constraint.subtarget = x.name.replace(".", "_T.")
    constraint.chain_count = 1
    
    # Set Up IK Limits
    x.lock_ik_x = False
    x.use_ik_limit_x = True
    x.ik_min_x = 0
    x.ik_max_x = math.pi / 60
    x.lock_ik_y = True
    x.lock_ik_z = True
    

logger.end()

