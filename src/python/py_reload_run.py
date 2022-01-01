# !BPY
# -*- coding: UTF-8 -*-
# Reload & Run Python
#
# 2019.03.30 N(Natukikazemizo)
#

import bpy
import os
import math

# CONSTANT OF PARAMETERS
# Python Name
PY_NAME = "create_folder_tree.py"

text = bpy.data.texts[PY_NAME]
ctx = bpy.context.copy()
ctx["edit_text"] = text

print("### Reload:" + PY_NAME)
bpy.ops.text.reload(ctx)
print("### Start" + PY_NAME)
bpy.ops.text.run_script(ctx)
print("### End" + PY_NAME)

