#!BPY
# -*- coding: UTF-8 -*-
# 
# read/write file
#
#
# 2017.08.29 Natukikazemizo
import bpy
import codecs


data =[]

f_in = codecs.open(bpy.path.abspath("//") + "data/in.txt", 'r', 'utf-8')
f_out = codecs.open(bpy.path.abspath("//") + "data/out.txt", 'w', 'utf-8')

data1 = f_in.read()
f_in.close()
lines1 = data1.split('n')
for line in lines1:
    data += line[:-2].split('\t')
    print(line)
    f_out.write(line)
f_out.close()

print(data)




