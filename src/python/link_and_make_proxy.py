#!BPY
# -*- coding: UTF-8 -*-
# LinkとProxyの作成
#
# 2021.06.27 N_natukikazemizo

import bpy

filepath = "C:/Blender/trunk/Sedna/Characters/DDEandN_cartoon/DDEandN_cartoon.blend"

work_collection_name = "WORK___"
colls_name = ["DDE", "N"]
objects_name = {"DDE":["CtrlPanel", "DDE_T", "Armature.DDE", "Byakue",
                "Byakue.Body", "Hibakama_Development", "Zori_Development"],
                "N":["Armature.N"]}
collections_name = {"DDE":["SubArmature", "Mesh"]}
proxy_target_name = ["Armature.DDE", "Armature.N"]

def make_collection(name):
    """ コレクション作成
    Keyword Arguments:
        name {str} -- 新規作成するコレクション名
    """
    if name not in bpy.data.collections:
        # 既存コレクションが存在した場合はコレクションを作成しない
         newCollection = bpy.data.collections.new(name)
         bpy.context.scene.collection.children.link(newCollection)

def move_object_collections(object_name, destination_name):
    """ オブジェクトを指定したコレクションに移動する
    なお，オブジェクトの他のコレクションへのリンクは削除する。

    Args:
        object_name (str): 移動対象のオブジェクト名
        destination_name (str): 移動先のコレクション名
    """

    selectob = bpy.data.objects.get(object_name)

    # 移動対象のオブジェクトが存在しなかった場合，何もしない
    if selectob == None:
        return

    destinationcollection = bpy.data.collections.get(destination_name)

    # 移動先のコレクションが存在しなかった場合，何もしない
    if destinationcollection == None:
        return

    # 既存のコレクションへのリンクてを全て削除
    for collection in bpy.data.collections:
        checklink = collection.objects.get(selectob.name)
        if checklink != None:
            collection.objects.unlink(selectob)

    # 指定されたコレクションへリンク
    destinationcollection.objects.link(selectob)

def move_collections_2_collections(from_col, to_col):
    """ コレクションを指定されたコレクションにリンクする
    他のコレクションへのリンクは全て削除する。

    Args:
        from_col (str): 移動対象のコレクション
        to_col (str): 移動先のコレクション
    """

    to_col_children = bpy.data.collections[to_col].children
    # 移動対象のコレクションが存在しなかった場合，何もしない
    if from_col in to_col_children:
        return

    # 既存のコレクションへのリンクを削除する。
    for collection in bpy.data.collections:
        if from_col in collection.children:
            checklink = collection.children[from_col]
            if checklink != None:
                collection.children.unlink(checklink)

    # 引数で指定されたコレクションへのリンクを作成
    to_col_children.link(bpy.data.collections[from_col])


def make_proxy(name):
    """ プロキシを作成する。
    Args:
        name:作成元のArmatureの名前
    """
    # 既存のプロキシは削除する。
    if name + "_proxy" in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects[name + "_proxy"])
    bpy.context.view_layer.objects.active = bpy.data.objects[name]
    bpy.ops.object.proxy_make()

for coll_name in colls_name:
    # filepathで指定したファイルからリンク対象のコレクションを取得
    with bpy.data.libraries.load(filepath, link=True) as (data_from, data_to):
        data_to.collections = [c for c in data_from.collections if c == coll_name]

    # コレクションをシーンにリンク
    for coll in data_to.collections:
        if coll is not None and coll.name not in bpy.data.collections:
           bpy.context.scene.collection.children.link(coll)

    # リンクしたコレクションにはオブジェクトを追加できないので，ワークコレクションを作成
    make_collection(work_collection_name)

    # ワークコレクションにオブジェクトを移動
    if coll_name in objects_name:
        for obj_name in objects_name[coll_name]:
            move_object_collections(obj_name, work_collection_name)

    # ワークコレクションにコレクション内コレクションを移動
    if coll_name in collections_name:
        for collection_name in collections_name[coll_name]:
            move_collections_2_collections(collection_name, work_collection_name)

    # リンクしたコレクションを削除
    bpy.data.collections.remove(bpy.data.collections[coll_name])
    # ワークコレクションをリンクしたコレクションの名称に変更
    bpy.data.collections[work_collection_name].name = coll_name

# プロキシを作成
for obj_name in proxy_target_name:
    make_proxy(obj_name)
