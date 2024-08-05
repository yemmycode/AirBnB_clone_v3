#!/usr/bin/python3
"""Module Documentation Checker
"""
import importlib
import sys

module_name = sys.argv[1]
module = importlib.import_module(module_name)

if module.__doc__:
    print("OK", end="")
else:
    print("No module documentation", end="")
