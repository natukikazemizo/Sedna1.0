import bpy


bl_info = {
    "name": "Test Target Addon",
    "author": "N(Natukikazemizo)",
    "version": (2, 0),
    "blender": (2, 79, 0),
    "location": "Object",
    "description": "Test Target Addon",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

# Translation dictionary
translation_dict = {
    "en_US": {
        ("*", "testee: Enabled add-on 'testee'"):
            "testee: Enabled add-on 'testee'",
        ("*", "testee: Disabled add-on 'testee'"):
            "testee: Disabled add-on 'testee'"
    },
    "ja_JP": {
        ("*", "testee: Enabled add-on 'testee'"):
            "テスト対象: アドオン「テスト対象」が有効化されました。",
        ("*", "testee: Disabled add-on 'testee'"):
            "テスト対象: アドオン「テスト対象」が無効化されました。"
    }
}
class TestOps1(bpy.types.Operator):

    bl_idname = "object.test_ops_1"
    bl_label = "Test1"
    bl_description = "Test target Operation1"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}


class TestOps2(bpy.types.Operator):

    bl_idname = "object.test_ops_2"
    bl_label = "Test2"
    bl_description = "Test target Operation2"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # オブジェクト名が「Cube」であるオブジェクトが存在しない場合
        if bpy.data.objects.find('Cube') == -1:
            return {'CANCELLED'}
        return {'FINISHED'}


def register():
    bpy.utils.register_module(__name__)
    # Register Translation dictionary
    bpy.app.translations.register(__name__, translation_dict)
    print(
        bpy.app.translations.pgettext(
            "testee: Enabled add-on 'testee'"
        )
    )

def unregister():
    # UnRegister Translation dictionary
    bpy.app.translations.unregister(__name__)
    bpy.utils.unregister_module(__name__)
    print(
        bpy.app.translations.pgettext(
            "testee: Disabled add-on 'testee'"
        )
    )



if __name__ == "__main__":
    register()
