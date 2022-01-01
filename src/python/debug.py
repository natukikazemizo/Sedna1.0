import sys

DEBUGGING = True

def start_debug():
    if DEBUGGING is True:
        PYDEV_SRC_DIR = "C:\pleiades\eclipse\plugins\org.python.pydev_4.5.3.201601211913\pysrc"
        # 環境に応じて書き換えが必要
        if PYDEV_SRC_DIR not in sys.path:
            sys.path.append(PYDEV_SRC_DIR)
            import pydevd
            pydevd.settrace()
            print("started blender script debugging...")
