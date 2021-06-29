#!BPY
# -*- coding: UTF-8 -*-
# Make Link and Make Proxy
#
# 2021.06.27 N_natukikazemizo

import bpy

filepath = "C:/Blender/trunk/Sedna/Characters/DDEandN_cartoon/DDEandN_cartoon.blend"

coll_name = "DDE"
coll_prxy_name = "DDE_prxy"
objects_name = ["CtrlPanel", "DDE_T", "Armature.DDE", "Byakue",
                "Byakue.Body", "Hibakama_Development", "Zori_Development"]
collections_name = ["SubArmature", "Mesh"]

def make_collection(arg):
    """ Make Collection
    Keyword Arguments:
        arg {str} -- New Collection's name.
    """
    if arg not in bpy.data.collections:
         newCollection = bpy.data.collections.new(arg)
         bpy.context.scene.collection.children.link(newCollection)

def move_object_collections(arg_objectname, arg_destinationname):
    """ Move object to Collection
    other collections are removed .

    Args:
        arg_objectname (str): object name
        arg_destinationname (str): collection name
    """

    selectob = bpy.data.objects.get(arg_objectname)

    if selectob == None:
        return

    destinationcollection = bpy.data.collections.get(arg_destinationname)

    if destinationcollection == None:
        return

    for collection in bpy.data.collections:
        checklink = collection.objects.get(selectob.name)
        if checklink != None:
            collection.objects.unlink(selectob)
    destinationcollection.objects.link(selectob)

def move_collections_2_collections(from_col, to_col):
    """ Move collection to collection

    Args:
        from_col (str): destination collection name
        to_col (str): target collection name
    """

    to_col_children = bpy.data.collections[to_col].children
    if from_col in to_col_children:
        return

    for collection in bpy.data.collections:
        checklink = collection.children[from_col]
        if checklink != None:
            collection.children.unlink(from_col)
    
    to_col_children.link(bpy.data.collections[from_col])

    


# link all collections starting with 'MyCollection'
with bpy.data.libraries.load(filepath, link=True) as (data_from, data_to):
    data_to.collections = [c for c in data_from.collections if c == coll_name]

# link collection to scene collection
for coll in data_to.collections:
    if coll is not None and coll.name not in bpy.data.collections:
       bpy.context.scene.collection.children.link(coll)

make_collection(coll_prxy_name)
for obj_name in objects_name:
    move_object_collections(obj_name, coll_prxy_name)

for collection_name in collections_name:
    move_collections_2_collections(collection_name, coll_prxy_name)

bpy.data.collections.remove(bpy.data.collections[coll_name])
