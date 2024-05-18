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
# 定数
XML_PATH = "render_settings.xml"
CSV_PATH = "render_cut.csv"

def hide_collection(collection_name, hide):
    bpy.data.collections[collection_name].hide_viewport = hide
    bpy.data.collections[collection_name].hide_render = hide

def render(row:list[str], rendering,  test, production):
    if row[0] not in bpy.context.scene.timeline_markers:
        print("INFO: start marker not found:" + row[0])
        return
    if row[1] not in bpy.context.scene.timeline_markers:
        print("INFO: end marker not found:" + row[1])
        return

    frame_start = bpy.context.scene.timeline_markers[row[0]].frame
    if bool(test.find("enable").text):
        frame_end = frame_start + int(test.find("print").find("count").text) - 1
    else :
        frame_end = bpy.context.scene.timeline_markers[row[1]].frame
    
    for collection_name in eval(row[2]):
        hide_collection(collection_name, False)
    
    bpy.context.scene.render.fps = int(rendering.find("frame").find("fps").text)
    bpy.context.scene.frame_step = int(rendering.find("frame").find("step").text)
    bpy.context.scene.frame_start = frame_start
    if bool(test.find("enable").text):
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
        
    if bool(rendering.find("enable").text):
        bpy.ops.render.render(animation=True)

    for collection_name in eval(row[3]):
        hide_collection(collection_name, True)

    print("#### Render End    #### frame:" + str(frame_start) + \
        "-" + str(frame_end))



# main
# 主処理
print("######## START ########")

# Read XML
# XMLファイル読み込み
tree = ET.parse(bpy.path.abspath("//") + XML_PATH)
root = tree.getroot()
rendering = root.find("rendering")
test = root.find("test")
production = root.find("production")

workspace_name = rendering.find("workspace").text
if bpy.data.workspaces.find(workspace_name) != -1:
    bpy.context.window.workspace = \
        bpy.data.workspaces[workspace_name]

bpy.context.scene.render.resolution_percentage = \
    int(rendering.find("resolution_percentage").text)

# Read CSV and render
# CSVファイル読み込みとレンダー

with open(bpy.path.abspath("//") + CSV_PATH) as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        count+=1
        # Skip Title row.
        if count > 1:
            render(row, rendering, test, production)


print("######## END   ########")


