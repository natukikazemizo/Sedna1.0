# !BPY
# -*- coding: UTF-8 -*-
# Render
#
# Render with hide/show Collections
#
# 2022.11.25 Natukikazemizo
#

import bpy
import os
import math


# For run in Concole
#  bpy.data.collections["COLLECTION_NAME"].hide_viewport = False
#  bpy.data.collections["COLLECTION_NAME"].hide_render = False

# CONSTANTS
TEST_MODE = True
ENABLE_RENDER = False
test_print_cnt = 0
TEST_PATH = "//..\..\..\..\\renderResults\\DDE#0050_Test\\Test_"
RESULT_PATH = "//..\..\..\..\\renderResults\\DDE#0050\\DDE0050_"
FRAME_STEP = 1
FPS = 24
CAMERA = "Camera.Main"
SCENE_NAME = "root"

def hide_collection(collection_name, hide):
    bpy.data.collections[collection_name].hide_viewport = hide
    bpy.data.collections[collection_name].hide_render = hide

def render(start_marker_name, end_marker_name, show_collections, hide_collections):
    if start_marker_name not in bpy.context.scene.timeline_markers:
        print("start marker not found:" + start_marker_name)
        return
    if end_marker_name not in bpy.context.scene.timeline_markers:
        print("end marker not found:" + end_marker_name)
        return

    frame_start = bpy.context.scene.timeline_markers[start_marker_name].frame
    frame_end = bpy.context.scene.timeline_markers[end_marker_name].frame
    
    for collection_name in show_collections:
        hide_collection(collection_name, False)
    
    bpy.context.scene.render.fps = FPS
    bpy.context.scene.frame_step = FRAME_STEP
    bpy.context.scene.frame_start = frame_start
    if TEST_MODE:
        bpy.context.scene.frame_end = frame_start
        bpy.data.scenes[SCENE_NAME].render.filepath = TEST_PATH
    else:
        bpy.context.scene.frame_end = frame_end
        bpy.data.scenes[SCENE_NAME].render.filepath = RESULT_PATH

    bpy.context.scene.camera = bpy.data.objects[CAMERA]
    print("#### Render Start  #### " + start_marker_name + " frame:" + str(frame_start) + \
        "-" +str(frame_end))
        
    if ENABLE_RENDER:
        bpy.ops.render.render(animation=True)

    for collection_name in hide_collections:
        hide_collection(collection_name, True)

    print("#### Render End    #### frame:" + str(frame_start) + \
        "-" + str(frame_end))


    
    

# main

print("######## START ########")

#bpy.context.window.screen = bpy.data.screens['Render']

bpy.context.scene.render.resolution_percentage = 100


render("Check the dinner menu", "END_Check the dinner menu", [], [])


print("######## END   ########")


