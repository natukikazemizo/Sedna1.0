#!BPY
# -*- coding: UTF-8 -*-
# Since bones move arbitrarily by switching IK/FK,
# Convert the coordinates before IK/FK switching to 
# the coordinates after IK/FK switching.
# IK/FKの切り替えでボーンが勝手に動いてしまうので、
# IK/FK切替前の座標を、IK/FK切替後の座標に変換する。
#
# 2023.06.13 Natukikazemizo(N Mizo)
from enum import Enum
import bpy
import csv

# Coordinate Source
# 座標の取得元
class CoSrc(Enum):
    Bone = 1    # ボーン
    Origin = 2  # 原点

# Part of Bone
# ボーンの部位
class POB(Enum):
    Zero = 0
    Head = 1
    Tail = 2
    Location = 3

# 四肢
class Limb(Enum):
    Arm_L = 1
    Arm_R = 2
    Leg_L = 3
    Leg_R = 4

# 運動学
class Kinematics(Enum):
    IK = 1
    FK = 2

# 処理対象のArmature名
ARMATURE_NAME = "Armature.DDE"

# 処理対象Frame
ORG_FRAME = 2266
FRAME_OFFSET = 1

# IK/FK切替コントロールボーン名
ARM_PIN_L = "Arm_Pin.L"
ARM_PIN_R = "Arm_Pin.R"
LEG_PIN_L = "Leg_Pin.L"
LEG_PIN_R = "Leg_Pin.R"

# Path of Setting File
# 設定ファイルのフルパス
FILE_PATH = "C:\Sync\GitHub\Sedna1.0\src\python\convert_location_4_IK_FK.csv"

# FKモードに切り替えられたと判定する最小値
MIN_FK = 0.001
ORIGIN = Vector((0, 0, 0))

# ボーンの名前と座標の取得元と部位
class SrcNamePart:
    """
    constructor
    コンストラクタ

    Parameters
    ----------
    name : str
        name of bone
    src : CoordinateSrc
        Source of coordinate
    part : POB
        part of bone
    """
    def __init__(self, src, name, part):
        self.src = src
        self.name = name
        self.part = part

    """
    Get the coordinates according to the bone part
    ボーンの部位に応じた座標を取得する

    Parameters
    ----------
    armature : bpy_types.Object
        Armature to which the bone 
        whose coordinates are to be obtained belongs
    """
    def get_location(self, armature):
        loc = None

        if self.src == CoSrc.Bone:
            if self.part == POB.Head:
                loc = armature.pose.bones[self.name].head
            elif self.part == POB.Tail:
                loc = armature.pose.bones[self.name].tail
            elif self.part == POB.Location:
                loc = armature.pose.bones[self.name].location
        elif self.src == CoSrc.Origin:
            loc = ORIGIN

        return loc

# Bone Transformation
# ボーン変換
class BoneTrans:
    """
    constructor
    コンストラクタ

    Parameters
    ----------
    limb : Limb
        Limb to which the bone belongs
    src_name_part_IK : SrcNamePart
        Bone coordinate information used for IK
    src_name_part_FK : SrcNamePart
        Bone coordinate information used for FK
    """
    def __init__(self, limb, src_name_part_IK, src_name_part_FK):
        self.limb = limb
        self.src_name_part_IK = src_name_part_IK
        self.src_name_part_FK = src_name_part_FK

    """
    constructor
    コンストラクタ

    Parameters
    ----------
    armature : bpy_types.Object
        Armature to which the bone 
        whose coordinates are to be obtained belongs
    limb_kinematics : dict
        Dictionary of limb and kinematics(IK/FK)
    """
    def get_location(self, armature, limb_kinematics):
        if (limb_kinematics[self.limb]) == Kinematics.IK:
            return self.src_name_part_IK.get_location(armature)
        elif  (limb_kinematics[self.limb]) == Kinematics.FK:
            return self.src_name_part_FK.get_location(armature)

        return None

"""
    read csv file
    CSVファイルを

    Parameters
    ----------
    file_path : str
        file path
    enc : str
        file encoding
"""
def read_csv(file_path, enc = 'utf-8'):
    header = []
    data = [] 
    try:
        if enc == 'utf-8':        
            # utf-8 CSV File
            with open(file_path, 'r') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                header = next(csv_reader)
                for row in csv_reader:
                    data.append(row)
        else:
            # read arg encoding csv file
            with open(file_path, 'r', encoding = enc) as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                header = next(csv_reader)
                for row in csv_reader:
                    data.append(row)
    except FileNotFoundError as e:
        print(e)
    except csv.Error as e:
        print(e)
    return header, data


# Initializing variables
# 変数初期化

# dictionary of IK/FK switching bone names corresponding to limbs
# 四肢に対応するIK/FK切替ボーン名の辞書
limb_pin_bone = {Limb.Arm_L:ARM_PIN_L, Limb.Arm_R:ARM_PIN_R, \
         Limb.Leg_L:LEG_PIN_L, Limb.Leg_R:LEG_PIN_R}

# Creating a dictionary for bone coordinate transformation
# ボーンの座標変換用の辞書作成
bones_transformation = \
    {"Hand.L":BoneTrans(Limb.Arm_L,SrcNamePart(CoSrc.Origin, "", POB.Zero), \
                         SrcNamePart(CoSrc.Bone, "Hand_Rot.L", POB.Head)), \
     "Hand_Rot_T.L":BoneTrans(Limb.Arm_L, SrcNamePart(CoSrc.Bone, "Hand_Rot_T.L", POB.Head), SrcNamePart(CoSrc.Bone, "Hand_Rot.L", POB.Tail))}


#    "Hand_T.L":BoneTrans(Limb.Arm_L, SrcNamePart(CoSrc.Bone"Hand_T.L", POB.Head), SrcNamePart(CoSrc.Bone"Hand_T.L", POB.Head)),\
#    "Hand_P.L":BoneTrans(Limb.Arm_L, SrcNamePart(CoSrc.Bone"Hand_P.L", POB.Head), SrcNamePart(CoSrc.Bone"Hand_P.L", POB.Head)),\
#    "Elbo_T.L":BoneTrans(Limb.Arm_L, SrcNamePart(CoSrc.Bone"Humerus_L.001", POB.Tail), SrcNamePart(CoSrc.Bone"Elbo_T.L", POB.Head)),\
#    "Sleeve_T.L":BoneTrans(Limb.Arm_L, SrcNamePart(CoSrc.Bone"Sleeve_T.L", POB.Head), SrcNamePart(CoSrc.Bone"Sleeve_T.L", POB.Head)),\
#    "Ulna_P.L":BoneTrans(Limb.Arm_L, SrcNamePart(CoSrc.Bone"Ulna_P.L", POB.Head), SrcNamePart(CoSrc.Bone"Ulna_P.L", POB.Head)),\
#   "Hand.R":BoneTrans(Limb.Arm_R, SrcNamePart(CoSrc.Origin"-", POB.Zero), SrcNamePart(CoSrc.Bone"Hand_Rot.R", POB.Head)),\
#    "Hand_Rot_T.R":BoneTrans(Limb.Arm_R, SrcNamePart(CoSrc.Bone"Hand_Rot_T.R", POB.Head), SrcNamePart(CoSrc.Bone"Hand_Rot.R", POB.Tail)),\
#    "Hand_T.R":BoneTrans(Limb.Arm_R, SrcNamePart(CoSrc.Bone"Hand_T.R", POB.Head), SrcNamePart(CoSrc.Bone"Hand_T.R", POB.Head)),\
#    "Hand_P.R":BoneTrans(Limb.Arm_R, SrcNamePart(CoSrc.Bone"Hand_P.R", POB.Head), SrcNamePart(CoSrc.Bone"Hand_P.R", POB.Head)),\
#    "Elbo_T.R":BoneTrans(Limb.Arm_R, SrcNamePart(CoSrc.Bone"Humerus_L.001", POB.Tail), SrcNamePart(CoSrc.Bone"Elbo_T.R", POB.Head)),\
#    "Sleeve_T.R":BoneTrans(Limb.Arm_R, SrcNamePart(CoSrc.Bone"Sleeve_T.R", POB.Head), SrcNamePart(CoSrc.Bone"Sleeve_T.R", POB.Head)),\
#    "Ulna_P.R":BoneTrans(Limb.Arm_R, SrcNamePart(CoSrc.Bone"Ulna_P.R", POB.Head), SrcNamePart(CoSrc.Bone"Ulna_P.R", POB.Head)),\
#    "Thigh_T.L":BoneTrans(Limb.Leg_L, SrcNamePart(CoSrc.Bone"Thigh.Tail.L", POB.Tail), SrcNamePart(CoSrc.Bone"Thigh_T.L", POB.Head)),\
#    "Knee_T.L":BoneTrans(Limb.Leg_L, SrcNamePart(CoSrc.Bone"Knee.L", POB.Tail), SrcNamePart(CoSrc.Bone"Knee_T.L", POB.Head)),\
#    "Tibia_P.L":BoneTrans(Limb.Leg_L, SrcNamePart(CoSrc.Bone"Tibia_P.L", POB.Head), SrcNamePart(CoSrc.Bone"Tibia_P.L", POB.Head)),\
#    "Foot_P.L":BoneTrans(Limb.Leg_L, SrcNamePart(CoSrc.Bone"Foot_P.L", POB.Head), SrcNamePart(CoSrc.Bone"Foot_P.L", POB.Head)),\
#    "Foot_Rot_T.L":BoneTrans(Limb.Leg_L, SrcNamePart(CoSrc.Bone"Foot_Rot.L", POB.Tail), SrcNamePart(CoSrc.Bone"Foot_Rot_T.L", POB.Head)),\
##    "Foot_T.L":BoneTrans(Limb.Leg_L, SrcNamePart(CoSrc.Bone"Foot_T.L", POB.Head), SrcNamePart(CoSrc.Bone"Foot_T.L", POB.Head)),\
 #   "Thigh_T.R":BoneTrans(Limb.Leg_R, SrcNamePart(CoSrc.Bone"Thigh.Tail.R", POB.Tail), SrcNamePart(CoSrc.Bone"Thigh_T.R", POB.Head)),\
 #   "Knee_T.R":BoneTrans(Limb.Leg_R, SrcNamePart(CoSrc.Bone"Knee.R", POB.Head), SrcNamePart(CoSrc.Bone"Knee_T.R", POB.Head)),\
 ##   "Tibia_P.R":BoneTrans(Limb.Leg_R, SrcNamePart(CoSrc.Bone"Tibia_P.R", POB.Head), SrcNamePart(CoSrc.Bone"Tibia_P.R", POB.Head)),\
  #  "Foot_P.R":BoneTrans(Limb.Leg_R, SrcNamePart(CoSrc.Bone"Foot_P.R", POB.Tail), SrcNamePart(CoSrc.Bone"Foot_P.R", POB.Head)),\
  #  "Foot_Rot_T.R":BoneTrans(Limb.Leg_R, SrcNamePart(CoSrc.Bone"Foot_Rot.R", POB.Head), SrcNamePart(CoSrc.Bone"Foot_Rot_T.R", POB.Head)),\
  #  "Foot_T.R":BoneTrans(Limb.Leg_R, SrcNamePart(CoSrc.Bone"Foot_T.R", POB.Head), SrcNamePart(CoSrc.Bone"Foot_T.R", POB.Head))}

bpy.context.scene.frame_current=FROM_FRAME

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


 