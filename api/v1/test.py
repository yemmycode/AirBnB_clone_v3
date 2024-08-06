#!/usr/bin/python3
"""Module Documentation Checker
"""
import importlib
import sys

if len(sys.argv) != 2:
    print("Usage: ./test.py <module_name>")
    sys.exit(1)

module_name = sys.argv[1]

try:
    module = importlib.import_module(module_name)
except ModuleNotFoundError:
    print(f"Error: No module named '{module_name}'")
    sys.exit(1)

if module.__doc__:
    print("OK", end="")
else:
    print("No module documentation", end="")
