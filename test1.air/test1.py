# -*- encoding=utf8 -*-
__author__ = "AirtestProject"

from airtest.core.api import *
from airtest.aircv import *
from airtest.core.android.android import *
from PIL import Image
import threading
import inspect
import ctypes

auto_setup(__file__)

connect_device("Android://127.0.0.1:5037/127.0.0.1:62001?cap_method=javacap")



for i in range(0,3):
    touch(Template(r"tpl1659349203549.png", threshold=0.9000000000000001, record_pos=(0.072, 0.069), resolution=(1600, 900)))
    sleep(5)

    result = wait(Template(r"tpl1659441810521.png", threshold=0.9000000000000001, rgb=False, record_pos=(0.074, 0.068), resolution=(1600, 900)))
    touch(result)