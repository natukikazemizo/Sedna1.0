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

def render(marker_name, frames, show_collections, hide_collections):
    if marker_name not in bpy.context.scene.timeline_markers:
        print("marker not found:" + marker_name)
        return
    frame_start = bpy.context.scene.timeline_markers[marker_name].frame
    frame_end = frame_start + frames - 1
    
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
    print("#### Render Start  #### " + marker_name + " frame:" + str(frame_start) + \
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


# 0000 Init 
#render("0000_Init", 0, [], ["FeatureTree", "Paintbrush", "PaintPlates", "WarnedSRC", \
#    "VCS", "RelatedDocuments", "HighlightedSourceCode", "SyncSrcAndTree"])
# 0010 N -> Rejected?
# render("0010_N", 300, [], [])
# 0020 N call DDE
# render("0020_N_call_DDE", 250, [], [])
# 0030 FeatureTree
# render("0030_FeatureTree", 600, ["FeatureTree"], ["FeatureTree"])
# 0040 Uninstall DDE
# render("0040_Uninstall_DDE", 700, [], [])
# 0050 Highlighted SRC
# render("0050_Highlighted_SRC", 300, ["HighlightedSourceCode"], ["HighlightedSourceCode"])
# 0060 SVN
# render("0060_SVN", 500, ["SVN","vcs"], ["SVN","vcs"])
# 0070 Call tree & editor
# 0070_CallTreeAndEditor
render("0070_CallTreeAndEditor", 300, [], ["VCS.001"])
# 0080 Sync Code And Tree
# render("0080_SyncCodeTree", 300, ["SyncSrcAndTree"], ["SyncSrcAndTree"])
# 0090 Warned SRC
# render("0090_WarnedSRC", 400, ["WarnedSRC"], ["WarnedSRC"])
# 0100 N And DDE
# render("0100_N_And_DDE", 300, [], [])
# 0110 DDE CHange
# render("0110_DDE_Transformation", 300, [], [])
# 0120 Projects
# render("0120_Projects", 600, [], [])


print("######## END   ########")


