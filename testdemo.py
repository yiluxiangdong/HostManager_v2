#!/usr/bin/python
#-*- coding:utf-8 _*-

import os

imagespath =  os.path.realpath('static\\images')
# for   images in os.listdir(os.path.realpath('static\\images')):
#     print os.path.join(imagespath,images)
#     os.remove(os.path.join(imagespath,images))


path = os.path.abspath('static/images')
print path,os.listdir(path)
print  os.path.splitext(os.listdir(path)[0])[-1]