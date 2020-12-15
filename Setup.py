# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 04:36:19 2020

@author: Piyush Chanchal
It is using CX_freeze library
"""



import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["tkinter","pandas","os"],"include_files":[(r'C:\Temp1\MyData\CSVs\Images',r"images")]}


# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "CSVsMerger",
        version = "1.0",
        description = "Desktop application which can merge two CSVs files into one.",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Main.py", base=base)])

options = {"build_exe": build_exe_options},