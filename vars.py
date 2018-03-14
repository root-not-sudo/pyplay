#!/usr/bin/env python
# # -*- coding: utf-8 -*-

'''prints the file location and version of python used'''
import sys
print(sys.executable)
print(sys.version)

'''function to return the memory address of a variable'''


def memory_address(in_var):
    return hex(id(in_var))
