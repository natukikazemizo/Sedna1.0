#!BPY
# -*- coding: UTF-8 -*-
# Copy Bone Constraints from Armature to another Armature
#
# 2017.10.15 Natukikazemizo
import bpy
import math
import os
import re
import utils_log

# init logger
global logger
logger = utils_log.Util_Log(os.path.basename(__file__))

logger.start()

toArmature = "Dorothy.Armature"

for from_bone in bpy.context.selected_pose_bones:
    if len(from_bone.constraints) > 0:
        to_bone = bpy.data.objects[toArmature].pose.bones[from_bone.name]
        print(to_bone.name + "Copy Constraints.")
        
        for from_constraint in from_bone.constraints:
            # Create New Constraint when none
            if from_constraint.name not in to_bone.constraints:
                newConstraint = to_bone.constraints.new(type=from_constraint.type)
                newConstraint.name = from_constraint.name 

            newConstraint = to_bone.constraints[from_constraint.name]
        
            if from_constraint.type == "IK":
                newConstraint.target = bpy.data.objects[toArmature]
                newConstraint.pole_target = from_constraint.pole_target
                newConstraint.subtarget = from_constraint.subtarget
                newConstraint.pole_angle =      from_constraint.pole_angle
                if from_constraint.pole_target is not None:
                    newConstraint.pole_target = bpy.data.objects[toArmature]
                    newConstraint.pole_subtarget = from_constraint.pole_subtarget
                newConstraint.iterations =      from_constraint.iterations
                newConstraint.chain_count =     from_constraint.chain_count
                newConstraint.use_tail =        from_constraint.use_tail
                newConstraint.use_stretch =     from_constraint.use_stretch
                newConstraint.use_location =    from_constraint.use_location
                newConstraint.use_rotation =    from_constraint.use_rotation
                newConstraint.weight =          from_constraint.weight
                newConstraint.orient_weight =   from_constraint.orient_weight
            elif y.type == "COPY_ROTATION":
                newConstraint.target_space =    from_constraint.target_space
                newConstraint.owner_space =     from_constraint.owner_space
                newConstraint.use_x =           from_constraint.use_x
                newConstraint.use_y =           from_constraint.use_y
                newConstraint.use_z =           from_constraint.use_z
                newConstraint.invert_x =        from_constraint.invert_x
                newConstraint.invert_y =        from_constraint.invert_y
                newConstraint.invert_z =        from_constraint.invert_z
                newConstraint.use_offset =      from_constraint.use_offset       

logger.end()

 