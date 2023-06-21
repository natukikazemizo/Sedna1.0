#!BPY
# -*- coding: UTF-8 -*-
# Since bones move arbitrarily by switching IK/FK,
# Convert the coordinates before IK/FK switching to 
# the coordinates after IK/FK switching.
# IK/FKの切り替えでボーンが勝手に動いてしまうので、
# IK/FK切替前の座標を、IK/FK切替後の座標に変換する。
#
# 2023.06.13 Natukikazemizo(Nミゾ)
from enum import Enum
import bpy
import csv
import os
import utils_log
import utils_io_csv

# Coordinate Source
# 座標の取得元
class CoordinateSrc(Enum):
    """Coordinate Source 
    座標の取得元
    """
    Bone = "Bone"    # ボーン
    Origin = "Origin"  # 原点

    def value_of(self, target_value):
        for e in CoordinateSrc:
            if e.value == target_value:
                return e
        raise ValueError('{}is not a valid value for CoordinateSrc!'\
                         .format(target_value))

class PartOfBone(Enum):
    """Part of Bone
    ボーンの部位"""
    Zero = "Zero"
    Head = "Head"
    Tail = "Tail"
    Location = "Location"

    def value_of(self, target_value):
        for e in PartOfBone:
            if e.value == target_value:
                return e
        raise ValueError('{}is not a valid value for PartOfBone!'\
                         .format(target_value))

class Limb(Enum):
    """Limb
    四肢
    """
    Arm_L = "Arm_L"
    Arm_R = "Arm_R"
    Leg_L = "Leg_L"
    Leg_R = "Leg_R"

    def value_of(self, target_value):
        for e in Limb:
            if e.value == target_value:
                return e
        raise ValueError('{}is not a valid value for Limb!'\
                         .format(target_value))

class Kinematics(Enum):
    """Kinematics
    運動学
    """
    IK = 1
    FK = 2

# 処理対象のArmature名
ARMATURE_NAME = "Armature.DDE"

# CSV Column Names
# CSVファイルの列名定義

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
SETTING_FILE_PATH = "C:\Sync\GitHub\Sedna1.0\src\python\convert_location_4_IK_FK.csv"

# FKモードに切り替えられたと判定する最小値
MIN_FK = 0.001
ORIGIN = Vector((0, 0, 0))

# Header Titles
# 列名
HEAD_BONE_NAME="bone_name"
HEAD_LIMB = "limb"
HEAD_SRC_IK = "src_IK"
HEAD_BONE_NAME_IK = "bone_name_IK"
HEAD_BONE_PART_IK = "bone_part_IK"
HEAD_SRC_FK = "src_FK"
HEAD_BONE_NAME_FK = "bone_name_FK"
HEAD_BONE_PART_FK = "bone_part_FK"

 
class SrcNamePart:
    """Source & name of bone & part of bone
    座標の取得元とボーンの名前とボーンの部位
    """

    def __init__(self, src, name, part):
        """
        Parameters
        ----------
        name : str
            name of bone
        src : CoordinateSrc
            Source of coordinate
        part : POB
            part of bone
        """

        self.src = src
        self.name = name
        self.part = part

    def get_location(self, armature):
        """Get the coordinates according to the bone part/
        ボーンの部位に応じた座標を取得する
        Parameters
        ----------
        armature : bpy_types.Object
            Armature to which the bone 
            whose coordinates are to be obtained belongs

        Returns
        -------
        class 'Vector' : Transformed Location
        """

        loc = None

        if self.src == CoordinateSrc.Bone:
            if self.part == PartOfBone.Head:
                loc = armature.pose.bones[self.name].head
            elif self.part == PartOfBone.Tail:
                loc = armature.pose.bones[self.name].tail
            elif self.part == PartOfBone.Location:
                loc = armature.pose.bones[self.name].location
        elif self.src == CoordinateSrc.Origin:
            loc = ORIGIN

        return loc

class BoneTrans:
    """ Bone coordinate Transformation
    ボーン座標変換
    """
    def __init__(self, limb, src_name_part_IK, src_name_part_FK):
        """
        Parameters
        ----------
        limb : Limb
            Limb to which the bone belongs
        src_name_part_IK : SrcNamePart
            Bone coordinate information used for IK
        src_name_part_FK : SrcNamePart
            Bone coordinate information used for FK
        """

        self.limb = limb
        self.src_name_part_IK = src_name_part_IK
        self.src_name_part_FK = src_name_part_FK

    def get_org_location(self, armature, kinematic) :
        """Get original location
        元座標取得
        Parameters
        ----------
        armature : bpy_types.Object
            Armature to which the bone 
            whose coordinates are to be obtained belongs
        kinematic : Kinematics
            coordinate target Kinematic(IK or FK)
        Returns
        -------
        class 'Vector' : Transformed Location
        """
        if kinematic == Kinematics.IK:
            return self.src_name_part_IK.get_location(armature)
        elif  kinematic == Kinematics.FK:
            return self.src_name_part_FK.get_location(armature)

        return None


    def get_location(self, armature, limb_kinematics):
        """Get Location
        座標取得
        Parameters
        ----------
        armature : bpy_types.Object
            Armature to which the bone 
            whose coordinates are to be obtained belongs
        limb_kinematics : dict
            Dictionary of limb and kinematics(IK/FK)
        Returns
        -------
        class 'Vector' : Transformed Location
        """

        if (limb_kinematics[self.limb]) == Kinematics.IK:
            return self.src_name_part_IK.get_location(armature)
        elif  (limb_kinematics[self.limb]) == Kinematics.FK:
            return self.src_name_part_FK.get_location(armature)

        return None

def check_IK_FK(amt, pin_bone_name):
    """Check IK or FK from pin_bone_name
            Parameters
        ----------
        armature : bpy_types.Object
            target armature
        pin_bone_name : str
            IK/FK controller bone's name
    """
    amt.pose.bones[pin_bone_name].location
    if amt.pose.bones[pin_bone_name].location.y > MIN_FK:
        return Kinematics.FK
    else:
        return Kinematics.IK


log = utils_log.UtilLog(os.path.basename(__file__))
log.start()

# Initializing variables
# 変数初期化

# dictionary of IK/FK switching bone names corresponding to limbs
# 四肢に対応するIK/FK切替ボーン名の辞書
limb_pin_bone = {Limb.Arm_L:ARM_PIN_L, Limb.Arm_R:ARM_PIN_R, \
         Limb.Leg_L:LEG_PIN_L, Limb.Leg_R:LEG_PIN_R}

# Get header and body data from configuration file
# 設定ファイルからヘッダと本体のデータ取得
header, body_rows = utils_io_csv.read(SETTING_FILE_PATH)

# Create column name dictionary from header row data
# ヘッダ行データから、列名辞書の作成
col_name_dic = {}
for i, val in enumerate(header):
    col_name_dic[i] = val

# Create a bone coordinate conversion dictionary 
# from the column name dictionary and body row data.
# 列名辞書と本体行データから、ボーン座標変換辞書を作成する。
bones_transformation = {}
for row in enumerate(body_rows):
    for i, col in enumerate(row):
        if col_name_dic[i] == HEAD_BONE_NAME:
            bone_name = col
        elif  col_name_dic[i] == HEAD_LIMB:
            row_limb = Limb.value_of(col)
        elif  col_name_dic[i] == HEAD_SRC_IK:
            src_ik = CoordinateSrc.value_of(col)
        elif  col_name_dic[i] == HEAD_BONE_NAME_IK:
            bone_name_ik = col
        elif  col_name_dic[i] == HEAD_BONE_PART_IK:
            bone_part_ik = PartOfBone.value_of(col)
        elif  col_name_dic[i] == HEAD_SRC_FK:
            src_fk = CoordinateSrc.value_of(col)
        elif  col_name_dic[i] == HEAD_BONE_NAME_FK:
            bone_name_fk = col
        elif  col_name_dic[i] == HEAD_BONE_PART_FK:
            bone_part_fk = PartOfBone.value_of(col)
    bones_transformation[bone_name] = BoneTrans(row_limb, \
            SrcNamePart(src_ik, bone_name_ik, bone_part_ik), \
            SrcNamePart(src_fk, bone_name_fk, bone_part_fk))

# In the original frame, get the coordinates 
# of the transformation source from the bone 
# of the armature and make it into a dictionary.
# 元フレームで、ArmatureのBoneから変換元の座標を取得し、辞書化する。
bpy.context.scene.frame_current = ORG_FRAME

amt = bpy.data.objects[ARMATURE_NAME]

org_coordinates = {}
for key in bones_transformation:
    bone_trans = bones_transformation[key]
    ik_fk_coordinates = {}
    # Get coordinate for IK
    # IK/FK用の座標を取得
    ik_fk_coordinates[Kinematics.IK] = bone_trans.get_org_location(amt, Kinematics.IK)
    ik_fk_coordinates[Kinematics.FK] = bone_trans.get_org_location(amt, Kinematics.FK)
    org_coordinates[key] = ik_fk_coordinates

# Set the coordinates after conversion in the destination frame
# 先フレームで、変換後の座標を設定する
bpy.context.scene.frame_current = ORG_FRAME + FRAME_OFFSET

limb_ik_fk = {}
limb_ik_fk[Limb.Arm_L] = check_IK_FK(amt, ARM_PIN_L)
limb_ik_fk[Limb.Arm_R] = check_IK_FK(amt, ARM_PIN_R)
limb_ik_fk[Limb.Leg_L] = check_IK_FK(amt, LEG_PIN_L)
limb_ik_fk[Limb.Leg_L] = check_IK_FK(amt, LEG_PIN_R)

for key in bones_transformation:
    amt.pose.bones[key].location = bones_transformation[key].get_location(amt, limb_ik_fk)

log.end()
