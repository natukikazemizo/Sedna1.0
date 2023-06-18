#!BPY
# -*- coding: UTF-8 -*-
# Log
#
# 2017.07.17 Natukikazemizo
import datetime

class UtilLog():
    def __init__(self, py_name):
        self.py_name = py_name

    def log(self, str):
        """Log datetime & str"""
        print(datetime.datetime.today().\
            strftime("%Y/%m/%d %H:%M:%S ") + self.py_name + " " + str)

    def detailtime_log(self, str):
        """Log ymdhms & str"""
        print(datetime.datetime.today().\
            strftime("%Y/%m/%d %H:%M:%S.%f ") + self.py_name + " " + str)

    def start(self):
        """Log start"""
        self.info("### START ###")

    def end(self):
        """Log end """
        self.info("### END   ###")

    def info(self, str):
        """Log info"""
        self.log("INFO:" + str)

    def warn(self, str):
        """Log warning"""
        self.log("WARN:" + str)

    def err(self, str):
        """Log error"""
        self.log("ERR :" + str)




