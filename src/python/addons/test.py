import bpy
import sys


bl_info = {
    "name": "Auto Test Test",
    "author": "N(Natukikazemizo)",
    "version": (0, 0),
    "blender": (2, 79, 0),
    "location": "None",
    "description": "Test of Auto Test",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Animation"
}

if __name__ == "__main__":
    try:
        # bl_name = object.test_ops_1 のテスト
        assert bpy.ops.object.test_ops_1 != None, "test_ops_1 is not enabled."
        result = bpy.ops.object.test_ops_1()
        assert result == {'FINISHED'}, "test_ops_1 have error."
        # bl_name = object.test_ops_2 のテスト
        assert bpy.ops.object.test_ops_2 != None, "test_ops_2 is not enabled."
        result = bpy.ops.object.test_ops_2()
        assert result == {'FINISHED'}, "test_ops_2 have error."
        ## bl_name = object.test_ops_3(存在しない) のテスト
        #assert bpy.ops.object.test_ops_3 != None, "test_ops_3 is not enabled."
        #result = bpy.ops.object.test_ops_3()
        #assert result == {'FINISHED'}, "test_ops_3 have error."
    # テスト失敗時の処理
    except AssertionError as e:
        print(e)        # テストが失敗した原因（assert文の第2引数）を表示
        sys.exit(1)     # Blenderを復帰値1で終了する
    # スクリプトの実行が正常に終了すると、Blenderは復帰値0で終了する
