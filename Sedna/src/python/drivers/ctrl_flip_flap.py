import bpy

def ctrl_flip_flap(x, p, offset):
    h = (x + p) % 1.00
    if h < 0.03:
        return 0 + offset
    elif h < 0.07:
        return (h - 0.03) * 4500 + offset
    elif h <= 0.1:
        return 180 + offset
    else:
        return h * 200 + 160 + offset

bpy.app.driver_namespace['ctrl_flip_flap'] = ctrl_flip_flap
