#!BPY
# -*- coding: UTF-8 -*-
# LinkとOverride Libraryの作成
#
# 2022.05.23 N_natukikazemizo

import bpy

filepath = "C:/Blender/trunk/Sedna/Characters/DDEandN_cartoon/DDEandN_cartoon.blend"

work_collection_name = "WORK___"
#collection_names = ["DDE", "N"]
collection_names = ["LinkLibTest"]
object_names = {"LinkLibTest":["Armature.LinkLibTest", "Cube.LinkLibTest"]}
#object_names = {"DDE":["CtrlPanel", "DDE_T", "Armature.DDE", "Byakue",
#                "Byakue.Body", "Hibakama_Development", "Zori_Development"],
#                "N":["Armature.N", "N", "N.LightBones"]}
collections_names = {"DDE":["SubArmature"]}
#armature_names = ["Armature.DDE", "Armature.N"]
armature_names = ["Armature.LinkLibTest"]

def make_collection(name):
    """ コレクション作成
    Keyword Arguments:
        name {str} -- 新規作成するコレクション名
    """
    if name not in bpy.data.collections:
        # 既存コレクションが存在した場合はコレクションを作成しない
         new_collection = bpy.data.collections.new(name)
         bpy.context.scene.collection.children.link(new_collection)

def move_object_collections(object_name, destination_name):
    """ オブジェクトを指定したコレクションに移動する
    なお，オブジェクトの他のコレクションへのリンクは削除する。

    Args:
        object_name (str): 移動対象のオブジェクト名
        destination_name (str): 移動先のコレクション名
    """

    selected_object = bpy.data.objects.get(object_name)

    # 移動対象のオブジェクトが存在しなかった場合，何もしない
    if selected_object == None:
        return

    destination_collection = bpy.data.collections.get(destination_name)

    # 移動先のコレクションが存在しなかった場合，何もしない
    if destination_collection == None:
        return

    # 既存のコレクションへのリンクてを全て削除
    for collection in bpy.data.collections:
        checklink = collection.objects.get(selected_object.name)
        if checklink != None:
            collection.objects.unlink(selected_object)

    # 指定されたコレクションへリンク
    destination_collection.objects.link(selected_object)

def move_collections_2_collections(from_collection, to_collection):
    """ コレクションを指定されたコレクションにリンクする
    他のコレクションへのリンクは全て削除する。

    Args:
        from_col (str): 移動対象のコレクション
        to_col (str): 移動先のコレクション
    """

    to_collection_children = bpy.data.collections[to_collection].children
    # 移動対象のコレクションが存在しなかった場合，何もしない
    if from_collection in to_collection_children:
        return

    # 既存のコレクションへのリンクを削除する。
    for collection in bpy.data.collections:
        if from_collection in collection.children:
            checklink = collection.children[from_collection]
            if checklink != None:
                collection.children.unlink(checklink)

    # 引数で指定されたコレクションへのリンクを作成
    to_collection_children.link(bpy.data.collections[from_collection])


def make_override_library(name):
    """ オーバーライドライブラリを作成する。
    Args:
        name:作成元のArmatureの名前
    """
    ## 既存のプロキシは削除する。
    #if name in bpy.data.objects:
    #    bpy.data.objects.remove(bpy.data.objects[name])
    bpy.data.objects[name].select_set(True)
    bpy.ops.object.make_override_library()

########################################################################
# Main処理
########################################################################
for collection_name in collection_names:
    # filepathで指定したファイルからリンク対象のコレクションを取得
    with bpy.data.libraries.load(filepath, link=True) as (data_from, data_to):
        data_to.collections = [c for c in data_from.collections if c == collection_name]

    # コレクションをシーンにリンク
    for collection in data_to.collections:
        if collection is not None and collection.name not in bpy.data.collections:
           bpy.context.scene.collection.children.link(collection)

    # リンクしたコレクションにはオブジェクトを追加できないので，ワークコレクションを作成
    make_collection(work_collection_name)

    # ワークコレクションにオブジェクトを移動
    if collection_name in object_names:
        for obj_name in object_names[collection_name]:
            move_object_collections(obj_name, work_collection_name)

    # ワークコレクションにコレクション内コレクションを移動
    if collection_name in collections_names:
        for collection_name in collections_names[collection_name]:
            move_collections_2_collections(collection_name, work_collection_name)

    # リンクしたコレクションを削除
    bpy.data.collections.remove(bpy.data.collections[collection_name])
    # ワークコレクションをリンクしたコレクションの名称に変更
    bpy.data.collections[work_collection_name].name = collection_name

# オーバーライドライブラリを作成
for obj_name in armature_names:
    make_override_library(obj_name)
