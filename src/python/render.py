# !BPY
# -*- coding: UTF-8 -*-
# Render
#
# Render with hide/show Collections
#
# Major changes 主な変更履歴
# 2022.11.25 Natukikazemizo Create New.
#                           新規作成
# 2024.05.16 N-mizo Change parameters to separate file.
#                   パラメータを別ファイルに変更
#

import bpy
import csv
import os
import math
import xml.etree.ElementTree as ET

# CONSTANTS
XML_PATH = "render_settings.xml"
CSV_PATH = "render_cut.csv"

def hide_collection(collection_name, hide):
    bpy.data.collections[collection_name].hide_viewport = hide
    bpy.data.collections[collection_name].hide_render = hide

def render(row:list[str], rendering,  test, production):
    if row[0] not in bpy.context.scene.timeline_markers:
        print("start marker not found:" + row[0])
        return
    if row[1] not in bpy.context.scene.timeline_markers:
        print("end marker not found:" + row[1])
        return

    frame_start = bpy.context.scene.timeline_markers[row[0]].frame
    if test.find("enable").text:
        frame_end = frame_start + test.find("print").find("count").text - 1
    else :
        frame_end = bpy.context.scene.timeline_markers[row[1]].frame
    
    for collection_name in row[2]:
        hide_collection(collection_name, False)
    
    bpy.context.scene.render.fps = rendering.find("frame").find("fps").text
    bpy.context.scene.frame_step = rendering.find("frame").find("step").text
    bpy.context.scene.frame_start = frame_start
    if test.find("enable").text:
        bpy.context.scene.frame_end = frame_start
        bpy.data.scenes[rendering.find("scene").text].render.filepath = \
            test.find("output").find("path").text
    else:
        bpy.context.scene.frame_end = frame_end
        bpy.data.scenes[rendering.find("scene").text].render.filepath = \
            production.find("output").find("path").text

    bpy.context.scene.camera = bpy.data.objects[rendering.find("camera").text]
    print("#### Render Start  #### " + row[0] + " frame:" + str(frame_start) + \
        "-" +str(frame_end))
        
    if rendering.find("enable").text:
        bpy.ops.render.render(animation=True)

    for collection_name in row[3]:
        hide_collection(collection_name, True)

    print("#### Render End    #### frame:" + str(frame_start) + \
        "-" + str(frame_end))



# main
print("######## START ########")

# Read XML
tree = ET.parse('country.xml')
root = tree.getroot()
rendering = root.find("render")
test = root.find("test")
production = root.find("production")


bpy.context.window.screen = \
    bpy.data.screens[rendering.find("screen").text]

bpy.context.scene.render.resolution_percentage = \
    rendering.find("resolution_percentage").text

# Read CSV and render

with open(CSV_PATH) as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        count+=1
        # Skip Title row.
        if count > 1:
            render(row, rendering, test, production)


print("######## END   ########")


