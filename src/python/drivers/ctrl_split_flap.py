#!BPY
# -*- coding: UTF-8 -*-
# ctrl_split_flap
#
# Calculate Split-flap display 's flaps angle
# 2020.09.03 N(Natukikazemizo)

import bpy

# period:period of Split-flap display (Seconds)
# pos:position of flip(0 start)
def ctrl_split_flap(x, num_of_flip, period, pos):
    
    p = period / num_of_flip * pos
    
    h = (x - p) % period
    
    angle_one = 180 / (num_of_flip -1)
    offset = angle_one * pos
    
    period_one = period / num_of_flip
    time_up = period_one * 0.3
    time_move_front = period_one * 0.7
    v_down = 180 / (period_one * 0.4)
    
    if h < time_up:
        return 0 + offset
    elif h < time_move_front:
        return (h - time_up) * v_down + offset
    elif h <= period_one:
        return 180 + offset
    else:
        return h * angle_one * num_of_flip + (180 - angle_one) + offset

bpy.app.driver_namespace['ctrl_split_flap'] = ctrl_split_flap
