# !BPY
# -*- coding: UTF-8 -*-
# Hide Collections
#
# Hide collections that are not used in the current scene
#
# 2023.01.14 Natukikazemizo
#

import bpy
import os
import math


# For run in Concole
#  bpy.data.collections["COLLECTION_NAME"].hide_viewport = False
#  bpy.data.collections["COLLECTION_NAME"].hide_render = False

# CONSTANTS

def hide_collection(collection_name, hide):
    bpy.data.collections[collection_name].hide_viewport = hide
    bpy.data.collections[collection_name].hide_render = hide

def hide(scene_name, show_collections, hide_collections):

#    if scene_name not in bpy.data.scenes:
#        print("scene not found:" + scene_name)
#        return

#    bpy.context.window.scene = bpy.data.scenes[scene_name]
    
    for collection_name in show_collections:
        hide_collection(collection_name, False)
    
    for collection_name in hide_collections:
        hide_collection(collection_name, True)



    
    

# main

print("######## START ########")

#bpy.context.window.screen = bpy.data.screens['Render']

bpy.context.scene.render.resolution_percentage = 100


# 0000 Init 
#hide("0000_Init", ["FeatureTree", "Paintbrush", "PaintPlates", "WarnedSRC", \
#    "VCS", "RelatedDocuments", "HighlightedSourceCode", "SyncSrcAndTree"], [])
# 0010 N -> Rejected?
# hide("0010_N", ["RelatedDocuments"], ["FeatureTree", "Paintbrush", "PaintPlates", "WarnedSRC", \
#    "VCS", "RelatedDocuments", "HighlightedSourceCode", "SyncSrcAndTree"])
# 0020 N call DDE
#hide("0020_N_call_DDE", ["RelatedDocuments"], [])
# 0026 DDE_Appear
hide("0025_N_call_DDE", [], ["RelatedDocuments"])
# 0030 FeatureTree
#hide("0030_FeatureTree", ["FeatureTree"], ["RelatedDocuments"])
# 0040 Uninstall DDE
#hide("0040_Uninstall_DDE", [], ["FeatureTree"])
# 0050 Highlighted SRC
#hide("0050_Highlighted_SRC", ["HighlightedSourceCode"], [])
# 0060 SVN
#hide("0060_SVN", ["VCS"], ["HighlightedSourceCode"])
# hide("0060_SVN", ["VCS","HighlightedSourceCode"], [])
# 0070 Emotional Exception
# hide("0070_EmotionalException", [], ["VCS"])
# 0080 Sync Code And Tree
# hide("0080_SyncCodeTree", ["SyncSrcAndTree"], [])
# 0090 Warned SRC
# hide("0090_WarnedSRC", ["WarnedSRC"], ["SyncSrcAndTree"])
# 0100 N And DDE
# hide("0100_N_And_DDE", [], ["WarnedSRC"])
# 0110 DDE CHange
# hide("0110_DDE_Transformation", [], [])
# 0120 Projects
# hide("0120_Projects", 600, [], [])


print("######## END   ########")


