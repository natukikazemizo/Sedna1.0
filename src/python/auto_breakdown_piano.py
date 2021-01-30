#!BPY
# -*- coding: UTF-8 -*-
# Auto BreakDown on Piano
#
# 2017.10.29 Natukikazemizo

import bpy
import os
import utils_log

# CONSTANTS
SCENE_NAME = "Root.DorothyLoris"
LEFT = "L"
RIGHT = "R"

ART_NORMAL = "NR"
ART_SLUR = "SL"
ART_TENUTO = "TN"
ART_STACCATO = "ST"

# Articulation Dictionary
ART_DIC = {
    ART_NORMAL:[1, -2],
    ART_SLUR:[1, -1],
    ART_TENUTO:[1, -1],
    ART_STACCATO:[1, 2]
}

START_FRAME = 3048
LORIS_R_START_FRAME = 3120
LORIS_L_START_FRAME = 3228
#END_FRAME = 3095
END_FRAME = 6800
FRAME_PAR_MEASURE = 48
MEASURE = 2

LH_NOTE_THUMB = ["Thumb_T.L.001"]

LH_NOTE_INDEX_2_LITTLE = [
    "Index_T.L.002",
    "Middle_T.L.002",
    "Ring_T.L.002",
    "Little_T.L.002"]

LH_NOTE_CTRLS = LH_NOTE_THUMB + LH_NOTE_INDEX_2_LITTLE

RH_NOTE_THUMB = ["Thumb_T.R.001"]

RH_NOTE_INDEX_2_LITTLE = [
    "Index_T.R.002",
    "Middle_T.R.002",
    "Ring_T.R.002",
    "Little_T.R.002"]

RH_NOTE_CTRLS = RH_NOTE_THUMB + RH_NOTE_INDEX_2_LITTLE

AUTO_BONE_LIST = LH_NOTE_CTRLS + RH_NOTE_CTRLS

#Classes
class Art:
    def __init__(self, measure, art):
        self.measure = measure
        self.art = art

class NoteOnHand:
    def __init__(self, start_frame):
        self.start_frame = start_frame
        self.thumb = [-1, -1, -1]
        self.index = [-1, -1, -1]
        self.middle = [-1, -1, -1]
        self.ring = [-1, -1, -1]
        self.little = [-1, -1, -1]
        self.art = ""

    def set(self, bone_name, end_frame, art):
        if bone_name == "Thumb_T.L.001" or bone_name == "Thumb_T.R.001":
            self.thumb = end_frame
        elif bone_name == "Index_T.L.002" or bone_name == "Index_T.R.002":
            self.index = end_frame
        elif bone_name == "Middle_T.L.002" or bone_name == "Middle_T.R.002":
            self.middle = end_frame
        elif bone_name == "Ring_T.L.002" or bone_name == "Ring_T.R.002":
            self.ring = end_frame
        elif bone_name == "Little_T.L.002" or bone_name == "Little_T.R.002":
            self.little = end_frame
        if art != "":
            self.art = art


# PARAMETER
ARMATURE_NAME_LIST = ["Dorothy.Armature", "Loris.Armature"]

RH_ART = {
    "Dorothy.Armature":[
        Art(0.000, "NR"),
        Art(0.750, "ST"),
        Art(1.125, "NR"),
        Art(1.875, "ST"),
        Art(2.500, "NR"),
        Art(2.875, "ST"),
        Art(3.000, "NR"),
        Art(3.750, "TN"),
        Art(4.000, "NR"),
        Art(4.250, "ST"),
        Art(4.500, "NR"),
        Art(5.250, "ST"),
        Art(5.500, "NR"),
        Art(6.000, "ST"),
        Art(6.6875, "NR"),
        Art(6.875, "ST"),
        Art(7.6875, "NR"),
        Art(7.875, "ST"),
        Art(11.250, "NR"),
        Art(11.625, "ST"),
        Art(13.250, "NR"),
        Art(13.625, "ST"),
        Art(15.166, "NR"),
        Art(17.000, "ST"),
        Art(17.125, "NR"),
        Art(18.000, "ST"),
        Art(18.125, "NR"),
        Art(19.000, "ST"),
        Art(24.375, "NR"),
        Art(24.625, "ST"),
        Art(25.250, "SL"),
        Art(25.500, "NR"),
        Art(25.625, "ST"),
        Art(26.375, "NR"),
        Art(26.625, "ST"),
        Art(27.250, "SL"),
        Art(27.500, "NR"),
        Art(27.625, "ST"),
        Art(30.500, "NR"),
        Art(31.125, "ST"),
        Art(31.250, "NR"),
        Art(31.375, "ST"),
        Art(31.500, "NR"),
        Art(31.875, "ST"),
        Art(32.000, "NR"),
        Art(32.125, "ST"),
        Art(32.250, "NR"),
        Art(32.4375, "ST"),
        Art(36.500, "NR"),
        Art(37.000, "ST"),
        Art(38.000, "NR"),
        Art(39.000, "ST"),
        Art(39.125, "NR"),
        Art(40.000, "ST"),
        Art(40.125, "NR"),
        Art(52.000, "ST"),
        Art(57.375, "NR"),
        Art(57.625, "ST"),
        Art(58.250, "SL"),
        Art(58.500, "NR"),
        Art(58.625, "ST"),
        Art(59.375, "NR"),
        Art(59.625, "ST"),
        Art(60.250, "SL"),
        Art(60.500, "NR"),
        Art(60.625, "ST"),
        Art(63.500, "NR"),
        Art(64.125, "ST"),
        Art(64.250, "NR"),
        Art(64.375, "ST"),
        Art(64.500, "NR"),
        Art(64.875, "ST"),
        Art(65.000, "NR"),
        Art(65.125, "ST"),
        Art(65.250, "NR"),
        Art(65.4375, "ST"),
        Art(69.500, "NR"),
        Art(70.000, "ST"),
        Art(71.000, "NR"),
        Art(72.000, "ST"),
        Art(72.125, "NR"),
        Art(73.000, "ST"),
        Art(73.125, "NR"),
        Art(76.000, "ST"),
        Art(76.250, "NR"),
        Art(76.500, "ST")
    ],
    "Loris.Armature":[
        Art(0.000, "ST"),
        Art(1.625, "NR"),
        Art(2.375, "ST"),
        Art(3.000, "NR"),
        Art(3.375, "ST"),
        Art(3.750, "TN"),
        Art(4.000, "NR"),
        Art(4.250, "ST"),
        Art(4.500, "NR"),
        Art(5.250, "ST"),
        Art(5.500, "NR"),
        Art(6.125, "ST"),
        Art(6.250, "NR"),
        Art(6.375, "ST"),
        Art(6.500, "NR"),
        Art(6.875, "ST"),
        Art(7.000, "NR"),
        Art(7.125, "ST"),
        Art(7.250, "NR"),
        Art(7.375, "ST"),
        Art(7.500, "NR"),
        Art(7.875, "ST"),
        Art(8.000, "NR"),
        Art(32.4375, "ST"),
        Art(33.000, "NR"),
        Art(41.000, "ST"),
        Art(41.125, "NR"),
        Art(42.000, "ST"),
        Art(42.125, "NR"),
        Art(48.000, "ST"),
        Art(48.166, "NR"),
        Art(50.000, "ST"),
        Art(50.125, "NR"),
        Art(51.000, "ST"),
        Art(51.125, "NR"),
        Art(65.4375, "ST"),
        Art(66.000, "NR"),
        Art(76.000, "ST"),
        Art(76.250, "NR"),
        Art(76.500, "ST")
    ]
    }

LH_ART = {
    "Dorothy.Armature":[
        Art(0.000, "ST"),
        Art(3.750, "TN"),
        Art(4.000, "NR"),
        Art(4.250, "ST"),
        Art(4.500, "NR"),
        Art(5.250, "ST"),
        Art(5.500, "NR"),
        Art(8.000, "TN"),
        Art(15.000, "ST"),
        Art(15.166, "TN"),
        Art(16.000, "NR"),
        Art(17.000, "SL"),
        Art(17.125, "ST"),
        Art(17.250, "SL"),
        Art(17.375, "ST"),
        Art(17.500, "SL"),
        Art(17.625, "ST"),
        Art(17.750, "SL"),
        Art(17.875, "ST"),
        Art(18.000, "SL"),
        Art(18.125, "ST"),
        Art(18.250, "SL"),
        Art(18.375, "ST"),
        Art(18.500, "SL"),
        Art(18.625, "ST"),
        Art(18.750, "SL"),
        Art(18.875, "ST"),
        Art(19.000, "TN"),
        Art(30.500, "NR"),
        Art(31.000, "ST"),
        Art(31.6875, "NR"),
        Art(31.875, "ST"),
        Art(33.000, "TN"),
        Art(37.000, "ST"),
        Art(38.000, "TN"),
        Art(39.000, "SL"),
        Art(39.125, "ST"),
        Art(39.250, "SL"),
        Art(39.375, "ST"),
        Art(39.500, "SL"),
        Art(39.625, "ST"),
        Art(39.750, "SL"),
        Art(39.875, "ST"),
        Art(40.000, "SL"),
        Art(40.125, "ST"),
        Art(40.250, "SL"),
        Art(40.375, "ST"),
        Art(40.500, "SL"),
        Art(40.625, "ST"),
        Art(40.750, "SL"),
        Art(40.875, "ST"),
        Art(41.000, "NR"),
        Art(48.000, "ST"),
        Art(48.166, "TN"),
        Art(49.000, "NR"),
        Art(52.000, "TN"),
        Art(63.500, "NR"),
        Art(64.000, "ST"),
        Art(64.6875, "NR"),
        Art(64.875, "ST"),
        Art(66.000, "TN"),
        Art(70.000, "ST"),
        Art(71.000, "TN"),
        Art(72.000, "SL"),
        Art(72.125, "ST"),
        Art(72.250, "SL"),
        Art(72.375, "ST"),
        Art(72.500, "SL"),
        Art(72.625, "ST"),
        Art(72.750, "SL"),
        Art(72.875, "ST"),
        Art(73.000, "SL"),
        Art(73.125, "ST"),
        Art(73.250, "SL"),
        Art(73.375, "ST"),
        Art(73.500, "SL"),
        Art(73.625, "ST"),
        Art(73.750, "SL"),
        Art(73.875, "ST"),
        Art(74.000, "TN"),
        Art(76.000, "ST"),
        Art(76.250, "NR"),
        Art(76.500, "ST")
    ],
    "Loris.Armature":[
        Art(0.000, "TN"),
        Art(4.000, "NR"),
        Art(4.250, "ST"),
        Art(4.500, "NR"),
        Art(5.250, "ST"),
        Art(5.500, "NR"),
        Art(6.000, "ST"),
        Art(6.625, "NR"),
        Art(6.875, "ST"),
        Art(7.625, "NR"),
        Art(7.875, "ST"),
        Art(8.000, "NR"),
        Art(32.4375, "ST"),
        Art(33.000, "NR"),
        Art(48.000, "ST"),
        Art(48.166, "NR"),
        Art(50.000, "ST"),
        Art(50.125, "NR"),
        Art(51.000, "ST"),
        Art(51.125, "NR"),
        Art(65.4375, "ST"),
        Art(66.000, "NR"),
        Art(75.000, "TN"),
        Art(75.250, "NR"),
        Art(76.000, "ST"),
        Art(76.250, "NR"),
        Art(76.500, "ST")
    ]
}


#globals
global logger
global bones
global bodyModionDic
global lhNoteDic
global rhNoteDic


#functions
def find_data_path(bone_name_list, data_path):
    """find bone_name from from data_path"""
    for x in bone_name_list:
        if data_path == 'pose.bones["' + x + '"].location':
            return True, x
    return False, ""

def get_bone_name(data_path):
    """get bone name from data_path"""
    if "].location" in data_path:
        index = data_path.find('"')
        str = data_path[index + 1:]
        index = str.find('"')
        str = str[:index]
        return str
    else:
        return ""

def get_art(art_list, frame):
    """get art"""
    art = art_list[0].art
    for x in art_list:
        if x.measure * FRAME_PAR_MEASURE + START_FRAME > frame:
            break
        art = x.art
    return art

def is_play(bone_name, x, y, z):
    if bone_name in ["Thumb_T.L.001", "Thumb_T.R.001"]:
        if z < 0.002:
            return True
        else:
            return False
    elif bone_name in LH_NOTE_INDEX_2_LITTLE:
        if x > - 0.001:
            return True
        else:
            return False
    elif bone_name in RH_NOTE_INDEX_2_LITTLE:
        if x < 0.001:
            return True
        else:
            return False
    else:
        return False

def get_note_frames(frame, next_frame, art):
    frames = []
    start = 0
    leave = 0
    end = 0

    start =  frame - ART_DIC[art][0]

    if ART_DIC[art][1] > 0:
        end = frame + ART_DIC[art][1]
    else:
        end = next_frame + ART_DIC[art][1]

    if start + 2 > end:
        end = start + 2

    leave = end - 1

    return [start, leave, end]

def add_motion(fcurves, fcurve_index_dic, bone_name, art, motion):
    for i, index in enumerate(fcurve_index_dic[bone_name]):
        for x in sorted(motion.keys()):
            add_keyframe_point(fcurves[index].keyframe_points, x, motion[x][i])
        fcurves[index].update()

def add_keyframe_point(keyframe_points, frame, value):
    keyframe_points.add(1)
    index = len(keyframe_points) - 1
    keyframe_points[index].type =  "BREAKDOWN"
    keyframe_points[index].co =  frame, value
    keyframe_points[index].handle_left = frame - 0.5, 0
    keyframe_points[index].handle_right = frame + 0.5, 0


def create_breakdown(armature_name, fcurves, fcurve_index_dic, frame_list, index, handNoteDic, lr):
    frame = frame_list[index]
    next_frame = frame_list[index + 1]
    handDic = handNoteDic[frame_list[index]]
    print("lr:" + lr + " index:" + str(index + 1) + "frame:" + str(frame_list[index + 1]))
    next_handDic = handNoteDic[frame_list[index + 1]]

    if (armature_name == "Dorothy.Armature" and frame >= START_FRAME and frame <= END_FRAME) or (armature_name == "Loris.Armature" and ((lr == LEFT and frame >= LORIS_L_START_FRAME and frame <= END_FRAME) or (lr == RIGHT and frame >= LORIS_R_START_FRAME and frame <= END_FRAME))):
        # SKIP when articulation is blank
        if handDic.art == "":
            return

        # set current frame
        bpy.context.scene.frame_set(frame)

        # get start/leave/end frame on hand
        start_list = []
        leave_list = []
        end_list = []
        lists = [start_list, leave_list, end_list]

        store_lists(handDic.thumb, lists)
        store_lists(handDic.index, lists)
        store_lists(handDic.middle, lists)
        store_lists(handDic.ring, lists)
        store_lists(handDic.little, lists)

        start_frame = min(start_list)
        leave_frame = max(leave_list)
        endng_frame = max(end_list)

        max_range = [start_frame, leave_frame, endng_frame]

        # create thumb motion
        bone_name = "Thumb_T." + lr + ".001"
        loc = bones[bone_name].location
        if handDic.thumb[0] == 0:
            motion = {start_frame:[loc[0], loc[1], loc[2] + 0.002],
                      leave_frame:[loc[0], loc[1], loc[2]],
                      endng_frame:[loc[0], loc[1], loc[2] + 0.0014]}
            add_motion(fcurves, fcurve_index_dic, bone_name, handDic.art, motion)
        elif handDic.thumb[0] > 0:
            if handDic.art == ART_STACCATO:
                motion = {handDic.thumb[0]:[loc[0], loc[1], loc[2] + 0.020],
                          handDic.thumb[2]:[loc[0], loc[1], loc[2] + 0.014]}
            else:
                motion = {handDic.thumb[0]:[loc[0], loc[1], loc[2] + 0.010],
                          handDic.thumb[1]:[loc[0], loc[1], loc[2] - 0.005],
                          handDic.thumb[2]:[loc[0], loc[1], loc[2] + 0.007]}
            add_motion(fcurves, fcurve_index_dic, bone_name, handDic.art, motion)

        # create index to little motion
        create_index2little_breakdown(fcurves, fcurve_index_dic, lr, "Index_T", handDic.index, max_range, handDic.art)
        create_index2little_breakdown(fcurves, fcurve_index_dic, lr, "Middle_T", handDic.middle, max_range, handDic.art)
        create_index2little_breakdown(fcurves, fcurve_index_dic, lr, "Ring_T", handDic.ring, max_range, handDic.art)
        create_index2little_breakdown(fcurves, fcurve_index_dic, lr, "Little_T", handDic.little, max_range, handDic.art)

        # get sign
        sign = 1
        if lr == RIGHT:
            sign = -1

        # add motion on Hand
        bone_name = "Hand_T." + lr
        loc = bones[bone_name].location
        if handDic.art == ART_STACCATO:
            hand_motion = {max_range[0]:[loc[0], loc[1] + 0.0010, loc[2]],
                           max_range[1]:[loc[0], loc[1] + 0.0007, loc[2]]}
        else:
            hand_motion = {max_range[0]:[loc[0], loc[1] + 0.00005, loc[2]],
                           max_range[1] + 1:[loc[0], loc[1], loc[2]],
                           max_range[2] + 1:[loc[0], loc[1] + 0.00010, loc[2]]}
                

        add_motion(fcurves, fcurve_index_dic, bone_name, handDic.art, hand_motion)

        # add motion on Arm
        bone_name = "Arm_T." + lr
        loc = bones[bone_name].location
        if handDic.art == ART_STACCATO:
            arm_motion = {max_range[0]:[loc[0] - sign * 0.010, loc[1], loc[2]],
                          max_range[1]:[loc[0] - sign * 0.007, loc[1], loc[2]]}
        else:
            arm_motion = {max_range[0]:[loc[0] - sign * 0.010, loc[1], loc[2]],
                          max_range[1]:[loc[0] - sign * 0.0049, loc[1], loc[2] - 0.003],
                          max_range[2]:[loc[0] - sign * 0.007, loc[1], loc[2]]}

        add_motion(fcurves, fcurve_index_dic, bone_name, handDic.art, arm_motion)

        ## add motion on Elbo
        #bone_name = "Elbo_T." + lr
        #loc = bones[bone_name].location
        #elbo_motion = {max_range[0] - 1:[loc[0] -sign * 0.005, loc[1] - 0.01, loc[2] + sign * 0.01],
        #               max_range[1] - 1:[loc[0], loc[1], loc[2]],
        #               max_range[2] - 1:[loc[0] -sign * 0.005, loc[1] - 0.01, loc[2] + sign * 0.01]}

        #add_motion(fcurves, fcurve_index_dic, bone_name, handDic.art, elbo_motion)

        # add motion on Shoulder_
        bone_name = "Shoulder_T." + lr
        loc = bones[bone_name].location
        shoulder_motion = {max_range[0] - 2:[loc[0], loc[1] + 0.0010, loc[2]],
                           max_range[1] - 2:[loc[0], loc[1], loc[2]],
                           max_range[2] - 2:[loc[0], loc[1] + 0.0008, loc[2]]}

        add_motion(fcurves, fcurve_index_dic, bone_name, handDic.art, shoulder_motion)


def create_index2little_breakdown(fcurves, fcurve_index_dic, lr, bone_name_key, finger_range, max_range, art):
    # get sign from lr
    sign = 1
    if lr == LEFT:
        sign = - 1

    # Add Finger 1st joints Motion
    bone_name = bone_name_key + "." + lr + ".002"
    loc = bones[bone_name].location

    if finger_range[0] == 0:
        motion = {max_range[0]:[loc[0] + 0.00015 * sign, loc[1], loc[2]],
                  max_range[1]:[loc[0], loc[1], loc[2]],
                  max_range[2]:[loc[0] + 0.0001 * sign, loc[1], loc[2]]}
        add_motion(fcurves, fcurve_index_dic, bone_name, art, motion)
    elif finger_range[0] > 0:
        if art == ART_STACCATO:
            motion = {finger_range[0]:[loc[0] + 0.002 * sign, loc[1], loc[2]],
                      finger_range[2]:[loc[0] + 0.001 * sign, loc[1], loc[2]]}
        else:
            motion = {finger_range[0]:[loc[0] + 0.0015 * sign, loc[1], loc[2]],
                      finger_range[1]:[loc[0] - 0.001 * sign, loc[1], loc[2]],
                      finger_range[2]:[loc[0] + 0.001 * sign, loc[1], loc[2]]}
        add_motion(fcurves, fcurve_index_dic, bone_name, art, motion)

    #  Add Finger 2nd joints Motion
    bone_name = bone_name_key + "." + lr + ".001"
    loc = bones[bone_name].location

    if finger_range[0] == 0:
        motion = {max_range[0]:[loc[0] + 0.000075 * sign, loc[1], loc[2]],
                  max_range[1]:[loc[0], loc[1], loc[2]],
                  max_range[2]:[loc[0] + 0.0005 * sign, loc[1], loc[2]]}
        add_motion(fcurves, fcurve_index_dic, bone_name, art, motion)
    elif finger_range[0] > 0:
        if art == ART_STACCATO:
            motion = {finger_range[0]:[loc[0] + 0.0002 * sign, loc[1], loc[2]],
                      finger_range[2]:[loc[0] + 0.0001 * sign, loc[1], loc[2]]}
        else:
            motion = {finger_range[0]:[loc[0] + 0.00015 * sign, loc[1], loc[2]],
                      finger_range[1]:[loc[0] + 0.001 * sign, loc[1], loc[2]],
                      finger_range[2]:[loc[0] + 0.0001 * sign, loc[1], loc[2]]}
        add_motion(fcurves, fcurve_index_dic, bone_name, art, motion)

    #  Add Finger 3rd joints Motion
    bone_name = bone_name_key + "." + lr
    loc = bones[bone_name].location

    if finger_range[0] == 0:
        motion = {max_range[0]:[loc[0] - 0.0001 * sign, loc[1], loc[2]],
                  max_range[1]:[loc[0], loc[1], loc[2]],
                  max_range[2]:[loc[0] - 0.000125 * sign, loc[1], loc[2]]}
        add_motion(fcurves, fcurve_index_dic, bone_name, art, motion)
    elif finger_range[0] > 0:
        if art == ART_STACCATO:
            motion = {finger_range[0]:[loc[0] - 0.001 * sign, loc[1], loc[2]],
                      finger_range[2]:[loc[0] - 0.0005 * sign, loc[1], loc[2]]}
        else:
            motion = {finger_range[0]:[loc[0] - 0.001 * sign, loc[1], loc[2]],
                      finger_range[1]:[loc[0] + 0.0001 * sign, loc[1], loc[2]],
                      finger_range[2]:[loc[0] - 0.00125 * sign, loc[1], loc[2]]}
        add_motion(fcurves, fcurve_index_dic, bone_name, art, motion)

def store_lists(frames, lists):
    if frames[0] > 0:
        lists[0].append(frames[0])
    if frames[1] > 0:
        lists[1].append(frames[1])
    if frames[2] > 0:
        lists[2].append(frames[2])


def auto_breakdown(armature_name):
    global bones
    global bodyModionDic
    global lhNoteDic
    global rhNoteDic
    bones = bpy.data.objects[armature_name].pose.bones
    bodyModionDic = {}
    lhNoteDic = {}
    rhNoteDic = {}


    cnt = 0
    axis = ""
    keyframeDic = {}
    fcurveList = []
    fcurve_index_dic = {}

    act = bpy.data.objects[armature_name].animation_data.action

    # delete all old breakdowns and create fcurve_index_dictionary
    for fcurve_index, x in enumerate(act.fcurves):
        oldBreakdownList = []

        bone_name = get_bone_name(x.data_path)

        if bone_name != "":
            if bone_name in fcurve_index_dic:
                fcurve_index_dic[bone_name].append(fcurve_index)
            else:
                fcurve_index_dic.update({bone_name:[fcurve_index]})

        for i, y in enumerate(x.keyframe_points):
            if y.type == "BREAKDOWN":
                oldBreakdownList.append(i)

        if len(oldBreakdownList) > 0:
            oldBreakdownList.reverse()
            for y in oldBreakdownList:
                x.keyframe_points.remove(x.keyframe_points[y])
            x.update()


    # create frame dic on hands
    for fcurve_index, x in enumerate(act.fcurves):
        if cnt == 0:
            keyframeDic = {}
            fcurveIndexList = []

        isFind, bone_name = find_data_path(AUTO_BONE_LIST, x.data_path)
        if isFind:
            keyframeList = []

            fcurveList.append(fcurve_index)

            cnt += 1
            if cnt == 1:
                axis = "X"
            if cnt == 2:
                axis = "Y"
            if cnt == 3:
                axis = "Z"
                cnt = 0

            # read all keyframe of ONE f-curve
            for i, y in enumerate(x.keyframe_points):
                if y.type == "KEYFRAME":
                    keyframeList.append([y.co[0], y.co[1]])

            # add keyframes on dic
            keyframeDic.update({axis:keyframeList})

            if axis == "Z":
                if bone_name in LH_NOTE_CTRLS or bone_name in RH_NOTE_CTRLS:
                    for i, y in enumerate(keyframeDic["X"]):
                        #SKIP LAST ELEMENT
                        if i == len(keyframeList) - 1:
                            break

                        frame = y[0]
                        loc_x = y[1]
                        loc_y = keyframeDic["Y"][i][1]
                        loc_z = keyframeDic["Z"][i][1]

                        #if is_play(bone_name, loc_x, loc_y, loc_z):
                        #    create_breakdown(armature_name, act.fcurves, fcurve_index_dic, bone_name, frame, \
                        #                  keyframeDic["X"][i + 1][0])

                        # create Note on hand dic
                        handDic = {}
                        if bone_name in LH_NOTE_CTRLS:
                            handDic = lhNoteDic
                        else:
                            handDic = rhNoteDic

                        if frame not in handDic:
                            handDic.update({frame:NoteOnHand(frame)})

                        frames = [0, 0, 0]
                        art = ""
                        if is_play(bone_name, loc_x, loc_y, loc_z):
                            if bone_name in LH_NOTE_CTRLS:
                                art = get_art(LH_ART[armature_name], frame)
                            else:
                                art = get_art(RH_ART[armature_name], frame)
                            frames = get_note_frames(frame, keyframeDic["X"][i + 1][0], art)

                        handDic[frame].set(bone_name, frames, art)

    # create lh breakdown
    frame_list = sorted(lhNoteDic.keys())
    for index in range(len(frame_list)- 1):
        create_breakdown(armature_name, act.fcurves, fcurve_index_dic, frame_list, index, lhNoteDic, LEFT)

    # create rh breakdown
    frame_list = sorted(rhNoteDic.keys())
    for index in range(len(frame_list)- 1):
        create_breakdown(armature_name, act.fcurves, fcurve_index_dic, frame_list, index, rhNoteDic, RIGHT)


# init logger
logger = utils_log.Util_Log(os.path.basename(__file__))

logger.start()

for x in ARMATURE_NAME_LIST:
    print(x)
    auto_breakdown(x)

logger.end()

