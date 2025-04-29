# !BPY
# -*- coding: UTF-8 -*-
#
# .blend ファイルの出力フォルダの
# 絶対パス一覧を出力する
#
# Major changes 主な変更履歴
# 2025.04.29 N-mizo 新規作成
#


import bpy
import codecs
import datetime
import os

TARGET_DIRECTORY = 'D:\\Blender\\trunk\\Sedna\\Animation'
OUTPUT_FILE = 'D:\\Blender\\trunk\\Sedna\\tmp\\output_folder_result.txt'

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
                
                # Clear the current scene and open a new file
                # 現在のシーンをクリアして新しいファイルを開く
                bpy.ops.wm.read_factory_settings(use_empty=True)
                bpy.ops.wm.open_mainfile(filepath=full_path)

                output_path = bpy.context.scene.render.filepath
                print_and_fo(f_out, full_path + f": " + output_path)
                
                # Close the file (returning to a new empty scene)
                # ファイルを閉じる（新しい空のシーンに戻す）
                bpy.ops.wm.read_factory_settings(use_empty=True)

    print_and_fo(f_out, str(datetime.datetime.now()) + " :### END #####")
    f_out.close()


# Run script
# スクリプトの実行
open_blend_files(TARGET_DIRECTORY)