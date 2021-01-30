# !BPY
# -*- coding: UTF-8 -*-
# Create Folder Tree
#
# Create Objects & Expnasion Motion
#
# 2019.03.12 Natukikazemizo
#

import bpy
import os
import math

# CONSTANT OF PARAMETERS
FOLDER_SPLITTER = "_"
SEED_FOLDER_NAME = 'Folder'
SEED_FOLDER_LEAF_NAME = 'Folder.Leaf'
SEED_FILE_NAME = 'File'
SEED_BRANCH_NAME = 'Branch'
ROOT_FOLDER = "C:/SRC/blender"
ROOT_FOLDER_ORG_NAME = "blender-2.79b"
# DEF FOR TEST
#ROOT_FOLDER = "C:/tmp/folder_tree_test/"
#ROOT_FOLDER_ORG_NAME = "root"
ROOT_FOLDER_SHORT_NAME = "Folder_0001"

ACTION_SUFFIX = 'Action'
SEED_ACTION = 'FolderAction'
FILE_SEED_ACTION = 'FileAction'

NEW_FOLDER_NAME = 'Folder_'
FOLDER_ZFILL = 4
NEW_FILE_NAME = 'File_'
FILE_ZFILL = 8
NEW_BRANCH_NAME = 'Branch_'
NEW_BRANCH_H_NAME = 'Branch_h_'
NEW_FOLDER_LEAF_NAME = "Folder.Leaf_"

START_FRAME = 3000
FPS = 12
SCALE_STORAGE = 0.5
SCALE_NORMAL = 1.0

# Folder Constants
FOLDER_X_POS_START = 0.02
FOLDER_X_POS_END = 0.2
FOLDER_X_MARGIN = 0.7
FOLDER_Y_MARGIN = 0.7
FOLDER_Z_MARGIN = 0.48
FOLDER_LEVEL1_Y_MARGIN = 2

FOLDER_STORAGE_SCALE = 0.02

FOLDER_FRAME_START_MARGIN = 1
FOLDER_FRAME_EXPAND_Z_WAIT = 0
FOLDER_FRAME_EXPAND_Z = 5
FOLDER_FRAME_EXPAND_X_WAIT = 1
FOLDER_FRAME_EXPAND_X = 6
FOLDER_FRAME_GO_OUT = 4
FOLDER_FRAME_RESIZE_WAIT = 1
FOLDER_FRAME_RESIZE = 4
FOLDER_FRAME_OPEN_WAIT = 1
FOLDER_FRAME_OPEN= 4
folder_motion_list = [
      FOLDER_FRAME_START_MARGIN
    , FOLDER_FRAME_EXPAND_Z_WAIT
    , FOLDER_FRAME_EXPAND_Z
    , FOLDER_FRAME_EXPAND_X_WAIT
    , FOLDER_FRAME_EXPAND_X
    , FOLDER_FRAME_GO_OUT
    , FOLDER_FRAME_RESIZE_WAIT
    , FOLDER_FRAME_RESIZE
    , FOLDER_FRAME_OPEN_WAIT
    , FOLDER_FRAME_OPEN
    ]

# Folder.Leaf Constants
FOLDER_REAF_X = 0
FOLDER_REAF_Y = -0.04
FOLDER_REAF_Z = -0.15682
FOLDER_REAF_OPEN = math.pi / 4


# Folder Name Constants
FOLDER_NAME_PREFIX = "FolderName_"

FOLDER_NAME_X_MARGIN = -0.2
FOLDER_NAME_Y_MARGIN = -0.2

FOLDER_NAME_SCALE_STOREGE = 0.03
FOLDER_NAME_ROT_X = -1 * math.pi / 9

FOLDER_NAME_FRAME_START_MARGIN = 48
FOLDER_NAME_FRAME_MOVE_X = 8
FOLDER_NAME_FRAME_RESIZE_WAIT = 4
FOLDER_NAME_FRAME_RESIZE = 8
FOLDER_NAME_FRAME_ROT_WAIT = 4
FOLDER_NAME_FRAME_ROT = 8

# Branch Constants
BRANCH_X_MARGIN = 0.5
BRANCH_Z_MARGIN = 0.2

# File Constants
FILE_X_MARGIN = 0.4
FILE_Y_MARGIN = 0
FILE_Z_MARGIN = 0

FILE_FRAME_START_MARGIN = 4
FILE_FRAME_Z_EXPAND = 12
FILE_FRAME_RESIZE_WAIT = 4
FILE_FRAME_RESIZE = 8
FILE_FRAME_X_ROT_WAIT = 4
FILE_FRAME_X_ROT = 8
FILE_FRAME_Y_EXPAND_WAIT = 4
FILE_FRAME_Y_EXPAND = 18

F_CURVE_X_LOC = 0
F_CURVE_Y_LOC = 1
F_CURVE_Z_LOC = 2
F_CURVE_X_ROT = 3
F_CURVE_Y_ROT = 4
F_CURVE_Z_ROT = 5
F_CURVE_X_SCA = 6
F_CURVE_Y_SCA = 7
F_CURVE_Z_SCA = 8
F_CURVE_ARRAY = 9

# Global dic
file_parent_dic = {}
folder_pos_dic = {ROOT_FOLDER_SHORT_NAME:("", 0, 0, 0)}
FOLDER_POS_PARENT_FOLDER_NAME = 0
FOLDER_POS_INDEX = 1
FOLDER_POS_LEVEL = 2
FOLDER_POS_ABSOLUTE_INDEX = 3

folder_num_name_dic = {"":"", ROOT_FOLDER_SHORT_NAME:ROOT_FOLDER_SHORT_NAME}
file_cnt_dic = {}
folder_end_frame_dic = {ROOT_FOLDER_SHORT_NAME:START_FRAME}

# Global list
level1_folder_list = []

# Global params
folder_absolute_index = 0

# File I/O
FOLDER_LIST_FILE_NAME="FolderList.txt"
root_path = bpy.path.abspath("//") + "data/"
text_file = open(root_path + FOLDER_LIST_FILE_NAME, mode = 'w')


def get_file_num_name(folder_name):
    folder_num_name = folder_num_name_dic[folder_name]
    file_num_name = NEW_FILE_NAME + folder_num_name[-FOLDER_ZFILL:]
    return file_num_name



def convert_folder_id(folder):

    ret = folder.replace(ROOT_FOLDER_ORG_NAME, ROOT_FOLDER_SHORT_NAME)
    ret = ret.replace(os.sep, FOLDER_SPLITTER)

    return ret

def clear_old_breakpoints(fcurve):
    old_keyframe_index_list = []

    for i, point in enumerate(fcurve.keyframe_points):
        if point.co[0] != START_FRAME:
            old_keyframe_index_list.append(i)

    if len(old_keyframe_index_list) > 0:
        old_keyframe_index_list.reverse()
        for i in old_keyframe_index_list:
            fcurve.keyframe_points.remove(fcurve.keyframe_points[i])
        fcurve.update()

def clear_all_old_breakpoints(fcurves):

    clear_old_breakpoints(fcurves[F_CURVE_X_LOC])
    clear_old_breakpoints(fcurves[F_CURVE_Y_LOC])
    clear_old_breakpoints(fcurves[F_CURVE_Z_LOC])
    clear_old_breakpoints(fcurves[F_CURVE_X_ROT])
    clear_old_breakpoints(fcurves[F_CURVE_Y_ROT])
    clear_old_breakpoints(fcurves[F_CURVE_Z_ROT])
    clear_old_breakpoints(fcurves[F_CURVE_X_SCA])
    clear_old_breakpoints(fcurves[F_CURVE_Y_SCA])
    clear_old_breakpoints(fcurves[F_CURVE_Z_SCA])

def clear_file_all_old_breakpoints(fcurves):
    clear_all_old_breakpoints(fcurves)
    clear_old_breakpoints(fcurves[F_CURVE_ARRAY])

def add_location_key_frame(fcurves, frame, x, y, z):
    add_keyframe_point(fcurves[F_CURVE_X_LOC], frame, x)
    add_keyframe_point(fcurves[F_CURVE_Y_LOC], frame, y)
    add_keyframe_point(fcurves[F_CURVE_Z_LOC], frame, z)

def add_rotation_key_frame(fcurves, frame, x, y, z):
    add_keyframe_point(fcurves[F_CURVE_X_ROT], frame, x)
    add_keyframe_point(fcurves[F_CURVE_Y_ROT], frame, y)
    add_keyframe_point(fcurves[F_CURVE_Z_ROT], frame, z)

def add_scale_key_frame(fcurves, frame, x, y, z):
    add_keyframe_point(fcurves[F_CURVE_X_SCA], frame, x)
    add_keyframe_point(fcurves[F_CURVE_Y_SCA], frame, y)
    add_keyframe_point(fcurves[F_CURVE_Z_SCA], frame, z)

def add_array_key_frame(fcurves, frame, val):
    add_keyframe_point(fcurves[F_CURVE_ARRAY], frame, val)


# get file list
file_list = []
for root, folders, files in os.walk(ROOT_FOLDER):
    root = os.path.relpath(root, ROOT_FOLDER)
    if root == '.': root = ''
    parent_folder = convert_folder_id(root)
    file_list.append([root, sorted(folders), sorted(files), parent_folder])


def print_file(file_name, level_list, last):
    """
    print fileName
    """
    t = ''

    if len(level_list): t += ' '

    if len(level_list) >= 2:
        for b in level_list[1:]:
            if b:
                t += ' '
            else:
                t += '|'

    if len(level_list):
        if last:
            t += '-'
        else:
            t += '+'

    print(t + file_name)
    text_file.write(t + file_name + '\n')

def dupObject(src_name, dup_name):
    """
    duplidate object
    """

    if bpy.data.objects.find(dup_name) < 0:
        src_obj = bpy.data.objects[src_name]

        # Select object
        bpy.ops.object.select_all(action='DESELECT')
        src_obj.select = True

        bpy.ops.object.duplicate(linked=True)
        new_obj = bpy.data.objects[src_name + '.001']
        new_obj.name = dup_name

def create_folder_num_name(folder_name):
    if folder_name not in folder_num_name_dic:
        folder_num_name_dic[folder_name] = NEW_FOLDER_NAME \
            + str(len(folder_num_name_dic) + 1).zfill(FOLDER_ZFILL)

def create_action(object_name):
    action_name = object_name + ACTION_SUFFIX
    if bpy.data.actions.find(action_name) < 0:
        new_action = bpy.data.actions[SEED_ACTION].copy()
        new_action.name = action_name
        bpy.data.objects[object_name].animation_data.action = new_action
    else:
        bpy.data.objects[object_name].animation_data.action = \
            bpy.data.actions[action_name]

def create_file_action(object_name):
    action_name = object_name + ACTION_SUFFIX
    # Enable Hire when f-cureve inclease .etc
    #if bpy.data.actions.find(action_name) > 0:
    #    bpy.data.actions.remove(bpy.data.actions[action_name])
    if bpy.data.actions.find(action_name) < 0:
        new_action = bpy.data.actions[FILE_SEED_ACTION].copy()
        new_action.name = action_name
        bpy.data.objects[object_name].animation_data.action = new_action
    else:
        bpy.data.objects[object_name].animation_data.action = \
            bpy.data.actions[action_name]


def get_branch_num_name(folder_name):
    folder_num_name = folder_num_name_dic[folder_name]
    return folder_num_name.replace(NEW_FOLDER_NAME, NEW_BRANCH_NAME)

def get_branch_h_num_name(folder_name):
    folder_num_name = folder_num_name_dic[folder_name]
    return folder_num_name.replace(NEW_FOLDER_NAME, NEW_BRANCH_H_NAME)

def get_folder_leaf_num_name(folder_name):
    folder_num_name = folder_num_name_dic[folder_name]
    return folder_num_name.replace(NEW_FOLDER_NAME, NEW_FOLDER_LEAF_NAME)

def get_folder_index(folder_num_name):
    if folder_num_name == ROOT_FOLDER_SHORT_NAME or folder_num_name == "":
        return 0
    return int(folder_num_name.replace(NEW_FOLDER_NAME, ""))

def create_folder_mesh(parent_folder_name, folder_name):
    """
    create folder mesh
    """

    create_folder_num_name(folder_name)

    # duplicate object
    num_name = folder_num_name_dic[folder_name]

    # delete org
    # Enable hire when you want to delete objects
    #if bpy.data.objects.find(num_name) > 0:
    #    bpy.ops.object.select_all(action= 'DESELECT')
    #    bpy.data.objects[num_name].select = True
    #    bpy.ops.object.delete()

    dupObject(SEED_FOLDER_NAME , num_name)

    # Enable Render
    bpy.data.objects[num_name].hide_render = False

    # Create new Action on new Object
    create_action(num_name)

    act = bpy.data.objects[num_name].animation_data.action

    # remove old keyframes
    clear_all_old_breakpoints(act.fcurves)

    # set start location
    add_location_key_frame(act.fcurves, START_FRAME, 0, 0, 0)

    # set start scale
    add_scale_key_frame(act.fcurves, START_FRAME, FOLDER_STORAGE_SCALE,\
        FOLDER_STORAGE_SCALE, FOLDER_STORAGE_SCALE)


def create_folder_leaf_mesh(parent_folder_name, folder_name):
    """
    create folder leaf mesh
    """

    # GetName
    folder_leaf_num_name = get_folder_leaf_num_name(folder_name)

    # delete org
    # Enable hire when you want to delete objects
    #if bpy.data.objects.find(folder_leaf_num_name) > 0:
    #    bpy.ops.object.select_all(action='DESELECT')
    #    bpy.data.objects[num_name].select = True
    #    bpy.ops.object.delete()

    dupObject(SEED_FOLDER_LEAF_NAME , folder_leaf_num_name)

    print(folder_leaf_num_name)
    set_obj_parent(folder_num_name_dic[folder_name], folder_leaf_num_name)

    # Enable Render
    bpy.data.objects[folder_leaf_num_name].hide_render = False

    # Create new Action on new Object
    create_action(folder_leaf_num_name)

    act = bpy.data.objects[folder_leaf_num_name].animation_data.action

    # remove old keyframes
    clear_all_old_breakpoints(act.fcurves)

    # set start location
    add_location_key_frame(act.fcurves, START_FRAME, FOLDER_REAF_X, \
        FOLDER_REAF_Y, FOLDER_REAF_Z)

    # set start rotation
    add_rotation_key_frame(act.fcurves, START_FRAME, 0, 0, 0)

    # set start scale
    add_scale_key_frame(act.fcurves, START_FRAME, 1, 1, 1)


def create_branch_mesh(parent_folder_name, folder_name):
    """
    create branch mesh
    """

    # duplicate object

    branch_num_name = get_branch_num_name(folder_name)

    dupObject(SEED_BRANCH_NAME , branch_num_name)

    # Enable Render
    bpy.data.objects[branch_num_name].hide_render = False

    # Create new Action on new Object
    create_action(branch_num_name)

    act = bpy.data.objects[branch_num_name].animation_data.action

    # remove old keyframes
    clear_all_old_breakpoints(act.fcurves)

    # set start location
    add_location_key_frame(act.fcurves, START_FRAME, 0, 0, 0)

    # set start scale
    add_scale_key_frame(act.fcurves, START_FRAME, SCALE_STORAGE, SCALE_STORAGE,\
        SCALE_STORAGE)

def create_branch_h_mesh(parent_folder_name, folder_name):
    """
    create branch mesh
    """

    # duplicate object

    branch_h_num_name = get_branch_h_num_name(folder_name)

    dupObject(SEED_BRANCH_NAME , branch_h_num_name)

    # Enable Render
    bpy.data.objects[branch_h_num_name].hide_render = False

    # Create new Action on new Object
    create_action(branch_h_num_name)

    act = bpy.data.objects[branch_h_num_name].animation_data.action

    # remove old keyframes
    clear_all_old_breakpoints(act.fcurves)

    # set start location
    add_location_key_frame(act.fcurves, START_FRAME, 0, 0, 0)

    # set start scale
    add_scale_key_frame(act.fcurves, START_FRAME, SCALE_STORAGE, SCALE_STORAGE,\
        SCALE_STORAGE)


def create_file_mesh(file_name):
    """
    create file mesh
    """

    # delete org
    # Enable hire when you want to delete objects
    #if bpy.data.objects.find(file_name) > 0:
    #    bpy.ops.object.select_all(action='DESELECT')
    #    bpy.data.objects[file_name].select = True
    #    bpy.ops.object.delete()

    # duplicate object
    dupObject(SEED_FILE_NAME , file_name)

    # Enable Render
    bpy.data.objects[file_name].hide_render = False

    # Create new Action on new Object
    create_file_action(file_name)

    act = bpy.data.objects[file_name].animation_data.action

    # remove old keyframes
    clear_file_all_old_breakpoints(act.fcurves)

    # set start location
    add_location_key_frame(act.fcurves, START_FRAME, 0, 0, 0)

    # set start rotation
    add_rotation_key_frame(act.fcurves, START_FRAME, 0, 0, 0)

    # set start scale
    add_scale_key_frame(act.fcurves, START_FRAME, SCALE_STORAGE, SCALE_STORAGE, SCALE_STORAGE)

    # set start array count
    add_array_key_frame(act.fcurves, START_FRAME, 1)

def set_obj_parent(parent_name, obj_name):
    """
    set parent on object
    """
    # set parent
    if parent_name != "":
        obj = bpy.data.objects[obj_name]

        # set parent
        obj.parent = bpy.data.objects[parent_name]


def func_main(arg, level_list):
    """
    MAIN
    """
    global folder_absolute_index
    root, folders, files, parent_folder = arg

    folder_len = len(folders)
    file_len = len(files)

    # Output subfolder

    for i, folder_name in enumerate(folders):
        nounder = (i == folder_len - 1 and file_len == 0)


        folder_id = folder_name
        # Replace root folder name to short name
        if folder_id == ROOT_FOLDER_ORG_NAME:
            folder_id = ROOT_FOLDER_SHORT_NAME

        if parent_folder != "":
            folder_id = parent_folder + FOLDER_SPLITTER + folder_id

        create_folder_mesh(parent_folder, folder_id)
        create_folder_leaf_mesh(parent_folder, folder_id)
        create_branch_mesh(parent_folder, folder_id)
        create_branch_h_mesh(parent_folder, folder_id)

        print_file('<' + folder_id + '>', level_list, nounder)

        level = len(level_list)
        folder_pos_dic[folder_id] = (parent_folder, i, level,  \
            folder_absolute_index)
        if level == 1:
            level1_folder_list.append(folder_id)

        folder_absolute_index += 1

        # Output subfolder's subfolder

        under_root = os.path.join(root, folder_name)
        under_list = []

        for t in file_list:
            if t[0] == under_root:
                under_list.append(t)

        for j, t in enumerate(under_list):
            if nounder and j == len(under_list) - 1:
                add = [True]
            else:
                add = [False]

            func_main(t, level_list + add)

    # Output files

    for i, file_name in enumerate(files):
        file_id = parent_folder + FOLDER_SPLITTER + file_name
        print_file(file_id, level_list, (i == file_len - 1))

    file_cnt = len(files)
    if file_cnt > 0:
        file_num_name = get_file_num_name(parent_folder)
        create_file_mesh(file_num_name)
        file_cnt_dic[parent_folder] = (file_num_name, file_cnt)

def add_keyframe_point(fcurve, frame, value):

    # find same frame keyframe_point
    index = 0
    find_frame = False
    for i, point in enumerate(fcurve.keyframe_points):
        if point.co[0] == frame:
            index = i
            find_frame = True
            break

    if find_frame == False:
        # add keyframe_point when same frame not found
        fcurve.keyframe_points.add(1)
        index = len(fcurve.keyframe_points) - 1

    # setup keyframe
    fcurve.keyframe_points[index].type =  "BREAKDOWN"
    fcurve.keyframe_points[index].co =  frame, value
    fcurve.keyframe_points[index].handle_left = frame - 0.5, value
    fcurve.keyframe_points[index].handle_right = frame + 0.5, value


def setupFolders(max_start_frame):

    # reset root folder size
    act = bpy.data.objects[ROOT_FOLDER_SHORT_NAME].animation_data.action
    # set start scale
    add_scale_key_frame(act.fcurves, 1000, SCALE_NORMAL, SCALE_NORMAL, SCALE_NORMAL)

    for folder_name, pos in folder_pos_dic.items():

        parent_folder_name, index, level, absolute_index = pos
        folder_num_name  = folder_num_name_dic[folder_name]

        folder_index = get_folder_index(folder_num_name);

        # Setup folder Name on Level 0, 1 Folders
        if level <= 1:
            # Get Folder Name Object's ID
            folder_name_id = FOLDER_NAME_PREFIX + folder_num_name

            # Set parent object
            set_obj_parent(folder_num_name, folder_name_id)

            # get fcurves
            fcurves = bpy.data.objects[folder_name_id].animation_data.action.fcurves

            # Clear old breakpoints
            clear_all_old_breakpoints(fcurves)

            # add Initial KeyFrame
            frame = START_FRAME
            add_location_key_frame(fcurves, frame, 0, 0, 0)
            add_rotation_key_frame(fcurves, frame, 0, 0, 0)
            add_scale_key_frame(fcurves, frame, FOLDER_NAME_SCALE_STOREGE, \
                FOLDER_NAME_SCALE_STOREGE, FOLDER_NAME_SCALE_STOREGE)

            # add Move x Start key Frame
            frame += (level + index) * sum(folder_motion_list) \
                + FOLDER_NAME_FRAME_START_MARGIN
            add_location_key_frame(fcurves, frame, 0, 0, 0)

            # add Move x End key Frame
            frame += FOLDER_NAME_FRAME_MOVE_X
            add_location_key_frame(fcurves, frame, FOLDER_NAME_X_MARGIN, \
                FOLDER_NAME_Y_MARGIN, 0)

            # add Resize wait key frame
            frame += FOLDER_NAME_FRAME_RESIZE_WAIT
            add_scale_key_frame(fcurves, frame, FOLDER_NAME_SCALE_STOREGE, \
                FOLDER_NAME_SCALE_STOREGE, FOLDER_NAME_SCALE_STOREGE)

            # add Resize end key frame
            frame += FOLDER_NAME_FRAME_RESIZE
            add_scale_key_frame(fcurves, frame, 1, 1, 1)

            # add Rotation wait key frame
            frame += FOLDER_NAME_FRAME_ROT_WAIT
            add_rotation_key_frame(fcurves, frame, 0, 0, 0)

            # add Rotaion end key frame
            frame += FOLDER_NAME_FRAME_ROT
            add_rotation_key_frame(fcurves, frame, FOLDER_NAME_ROT_X, 0, 0)

            fcurves.update()


        # set parent object
        branch_num_name = get_branch_num_name(folder_name)
        branch_h_num_name = get_branch_h_num_name(folder_name)

        if folder_name != ROOT_FOLDER_SHORT_NAME:
            set_obj_parent(folder_num_name_dic[parent_folder_name], branch_num_name)
            set_obj_parent(folder_num_name_dic[parent_folder_name], branch_h_num_name)
            set_obj_parent(folder_num_name_dic[parent_folder_name], folder_num_name)

        # Calclate folder relative index
        parent_absolute_index = 0

        if parent_folder_name != "":
            parent_absolute_index = \
                folder_pos_dic[parent_folder_name][FOLDER_POS_ABSOLUTE_INDEX]

        relative_index = absolute_index - parent_absolute_index

        if relative_index == 0:
            relative_index = 1

        # calc start frame
        parent_folder_index = 0
        if parent_folder_name != ROOT_FOLDER_SHORT_NAME :
            parent_folder_index = get_folder_index(folder_num_name_dic[parent_folder_name])

        frame = START_FRAME + (level + index) * sum(folder_motion_list)

        # get fcurves
        branch_fcurves = bpy.data.objects[branch_num_name].animation_data.action.fcurves
        brnc_h_fcurves = bpy.data.objects[branch_h_num_name].animation_data.action.fcurves
        folder_fcurves = bpy.data.objects[folder_num_name].animation_data.action.fcurves

        start_frame = frame
        # add move start key_frame
        frame +=  FOLDER_FRAME_START_MARGIN
        add_location_key_frame(branch_fcurves, frame, 0, 0, 0)
        add_rotation_key_frame(branch_fcurves, frame, 0, 0, 0)
        add_rotation_key_frame(brnc_h_fcurves, frame, 0, math.pi / 2, 0)
        add_location_key_frame(folder_fcurves, frame, 0, 0, 0)


        # add expand z wait key_frame
        frame += FOLDER_FRAME_EXPAND_Z_WAIT
        add_scale_key_frame(branch_fcurves, frame, 1, 1, 1)
        add_location_key_frame(brnc_h_fcurves, frame, 0, 0, 0)
        add_location_key_frame(folder_fcurves, frame, 0, 0, 0)

        # calc 1st Z add_location_key_frame
        z_loc_0010 = FOLDER_Z_MARGIN * index
        if folder_name == ROOT_FOLDER_SHORT_NAME:
            z_loc_0010 = FOLDER_Z_MARGIN * 2

        # add expand z end key_frame
        frame += FOLDER_FRAME_EXPAND_Z
        add_scale_key_frame(branch_fcurves, frame, 1, 1, z_loc_0010 * 100)
        add_location_key_frame(brnc_h_fcurves, frame, 0, 0, z_loc_0010)
        add_location_key_frame(folder_fcurves, frame, 0, 0, z_loc_0010)

        # add expand x wait key_frame
        frame += FOLDER_FRAME_EXPAND_X_WAIT
        add_scale_key_frame(brnc_h_fcurves, frame, 1, 1, 1)
        add_location_key_frame(folder_fcurves, frame, 0, 0, z_loc_0010)

        # add expand x end key_frame
        frame += FOLDER_FRAME_EXPAND_X
        add_scale_key_frame(brnc_h_fcurves, frame, 1, 1, \
            FOLDER_X_MARGIN * 100)
        add_location_key_frame(folder_fcurves, frame, FOLDER_X_MARGIN, 0, \
            z_loc_0010)

        # add go out key_frame
        frame += FOLDER_FRAME_GO_OUT
        add_location_key_frame(folder_fcurves, frame, \
            FOLDER_X_MARGIN + FOLDER_X_POS_START, 0, z_loc_0010)

        # add resize wait key_frame
        frame += FOLDER_FRAME_RESIZE_WAIT
        add_location_key_frame(folder_fcurves, frame,
            FOLDER_X_MARGIN + FOLDER_X_POS_START, 0, \
            z_loc_0010)
        add_scale_key_frame(folder_fcurves, frame, FOLDER_STORAGE_SCALE, \
            FOLDER_STORAGE_SCALE, FOLDER_STORAGE_SCALE)

        # add resize key_frame
        frame += FOLDER_FRAME_RESIZE
        add_location_key_frame(folder_fcurves, frame, \
            FOLDER_X_MARGIN + FOLDER_X_POS_END, 0, z_loc_0010)
        add_scale_key_frame(folder_fcurves, frame, SCALE_NORMAL, \
            SCALE_NORMAL, SCALE_NORMAL)

        # add folder motion end frame to dic
        folder_end_frame_dic[folder_name] = frame

        # add Z move end key frame
        z_loc_0020 = FOLDER_Z_MARGIN * relative_index
        if folder_name == ROOT_FOLDER_SHORT_NAME:
            z_loc_0020 = FOLDER_Z_MARGIN * 2

        frame = max_start_frame
        add_location_key_frame(folder_fcurves, frame, \
            FOLDER_X_MARGIN + FOLDER_X_POS_END, 0, z_loc_0020)
        add_location_key_frame(brnc_h_fcurves, frame, 0, 0, z_loc_0020)
        add_scale_key_frame(branch_fcurves, frame, 1, 1, z_loc_0020 * 100)



        # write log
        text_file.write(folder_num_name + "RelativeIndex:" + str(relative_index).zfill(4) \
            + "Level:" + str(level).zfill(3) \
            + "StartFrame:" + str(start_frame) + "EndFrame:" + str(frame) \
            + "index:" + str(index).zfill(3) \
            + "ParentFolder:" +  parent_folder_name + " MyName:" + folder_name \
            + '\n')

        # update fcurve
        branch_fcurves.update()
        folder_fcurves.update()



def setupFiles():
    for parent_folder, val in file_cnt_dic.items():

        file_num_name, file_cnt = val

        folder_leaf_num_name = get_folder_leaf_num_name(parent_folder)

        # Set parent object
        set_obj_parent(folder_num_name_dic[parent_folder], file_num_name)

        # get fcurves
        fcurves = bpy.data.objects[file_num_name].animation_data.action.fcurves
        folder_leaf_fcurves = \
            bpy.data.objects[folder_leaf_num_name].animation_data.action.fcurves

        # get start frame
        frame = folder_end_frame_dic[parent_folder]

        # add open wait key_frame
        frame += FOLDER_FRAME_OPEN_WAIT
        add_rotation_key_frame(folder_leaf_fcurves, frame, 0, 0, 0)

        # add open key_frame
        frame += FOLDER_FRAME_OPEN
        add_rotation_key_frame(folder_leaf_fcurves, frame, FOLDER_REAF_OPEN, \
             0, 0)

        # add move start key frame
        frame += FILE_FRAME_START_MARGIN
        add_location_key_frame(fcurves, frame, 0, 0, 0)

        # add z expand end keyFrame
        frame += FILE_FRAME_Z_EXPAND
        add_location_key_frame(fcurves, frame, FILE_X_MARGIN, 0, 0)

        # add resize wait keyFrame
        frame += FILE_FRAME_RESIZE_WAIT
        add_scale_key_frame(fcurves, frame, SCALE_STORAGE, SCALE_STORAGE, \
            SCALE_STORAGE)

        # add resize end keyFrame
        frame += FILE_FRAME_RESIZE
        add_scale_key_frame(fcurves, frame, SCALE_NORMAL, SCALE_NORMAL, \
            SCALE_NORMAL)

        # add x rot WAIT key frame
        frame += FILE_FRAME_X_ROT_WAIT
        add_rotation_key_frame(fcurves, frame, 0, 0, 0)

        # add x rot end key frame
        frame += FILE_FRAME_X_ROT
        add_location_key_frame(fcurves, frame, FILE_X_MARGIN, 0, 0)
        add_rotation_key_frame(fcurves, frame, math.pi, math.pi / 2, 0 )

        # add y expand wait key frame
        frame += FILE_FRAME_Y_EXPAND_WAIT
        add_array_key_frame(fcurves, frame, 1)

        # add y expand end key frame
        frame += FILE_FRAME_Y_EXPAND
        add_array_key_frame(fcurves, frame, file_cnt)

        # update fcurve
        fcurves.update()

# START
print("### start ###")
create_folder_mesh("", ROOT_FOLDER_SHORT_NAME)
func_main(file_list.pop(0), [])

# calc max start frame
max_start_frame = 0
for folder_name, pos in folder_pos_dic.items():
    parent_folder_name, index, level, absolute_index = pos
    frame = START_FRAME + (level + index) * sum(folder_motion_list)
    if frame > max_start_frame:
        max_start_frame = frame

setupFolders(max_start_frame)
setupFiles()
text_file.close()
print("### end ###")
