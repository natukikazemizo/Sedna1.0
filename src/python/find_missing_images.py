# !BPY
# -*- coding: UTF-8 -*-
#
# Find missing images
# リンク切れ画像探索
#
# Major changes 主な変更履歴
# 2025.03.01 N-mizo Create New with Grok3 of X
#                           X の Grok3で新規作成
#


import bpy
import datetime

def find_missing_images():
    print(str(datetime.datetime.now()) + " ### START ###")

    # A list to store the missing image paths
    # 見つからない画像パスを格納するリスト
    missing_images = []
    
    # Check out all materials
    # すべてのマテリアルをチェック
    for mat in bpy.data.materials:
        if mat.use_nodes:
            # If the node is used
            # ノードを使用している場合
            for node in mat.node_tree.nodes:
                # Check the image texture node
                # 画像テクスチャノードをチェック
                if node.type == 'TEX_IMAGE' and node.image:
                    img = node.image
                    # If the file path does not exist or cannot be found
                    # ファイルパスが存在しない、または見つからない場合
                    if img.filepath and (not bpy.path.abspath(img.filepath) or not bpy.data.images[img.name].has_data):
                        if img.filepath not in missing_images:
                            missing_images.append(img.filepath)
    
    # Output result
    # 結果の出力
    if missing_images:
        print("The following link broken images were found:")
        print("以下のリンク切れ画像が見つかりました:")
        for img_path in missing_images:
            print(f"- {img_path}")
    else:
        print("There were no link broken images.")
        print("リンク切れ画像はありませんでした。")
    print(str(datetime.datetime.now()) + " :### END #####")


# Run script
# スクリプトの実行
find_missing_images()
