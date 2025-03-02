# !BPY
# -*- coding: UTF-8 -*-
#
# Open Blender files
# 指定フォルダ配下の.blendファイルを開く
#
# Major changes 主な変更履歴
# 2025.03.02 N-mizo Create New with Grok3 of X
#                           X の Grok3で新規作成
#


import bpy
import codecs
import datetime
import os

TARGET_DIRECTORY = 'D:\\Blender\\trunk\\SednaSedna\\Animation\\Effects\\28Mansions'
OUTPUT_FILE = 'D:\\Blender\\trunk\\Sedna\\tmp\\result.txt'

def print_and_fo(f_out, text):
    print(text)
    f_out.write(text + "\r\n")
    
    

def open_blend_files(directory):
    f_out = codecs.open(OUTPUT_FILE, 'a', 'utf-8')
    print_and_fo(f_out, str(datetime.datetime.now()) + " ### START ###")

    # Search the specified directory and subfolders recursively
    # 指定したディレクトリとサブフォルダを再帰的に探索
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the extension is .blend
            # 拡張子が .blend かチェック
            if file.endswith(".blend"):
                full_path = os.path.join(root, file)
                print_and_fo(f_out, f"Opening: {full_path}")
                print_and_fo(f_out, f"開いています: {full_path}")
                
                # Clear the current scene and open a new file
                # 現在のシーンをクリアして新しいファイルを開く
                bpy.ops.wm.read_factory_settings(use_empty=True)
                bpy.ops.wm.open_mainfile(filepath=full_path)
                
                # Do something here (e.g. print the file name)
                # ここで何か処理を行う（例: ファイル名を出力）
                print_and_fo(f_out, f"Processing: {file}")
                print_and_fo(f_out, f"処理中: {file}")
                
                # Close the file (returning to a new empty scene)
                # ファイルを閉じる（新しい空のシーンに戻す）
                bpy.ops.wm.read_factory_settings(use_empty=True)
                print_and_fo(f_out, f"Closed: {full_path}")
                print_and_fo(f_out, f"閉じました: {full_path}")

    print_and_fo(f_out, str(datetime.datetime.now()) + " :### END #####")
    f_out.close()


# Run script
# スクリプトの実行
open_blend_files(TARGET_DIRECTORY)