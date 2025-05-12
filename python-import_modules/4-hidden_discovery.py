#!/usr/bin/python3
import sys
import importlib.util

if __name__ == "__main__":
    # Load the compiled Python file hidden_4.pyc
    path_to_pyc = '/tmp/hidden_4.pyc'
    spec = importlib.util.spec_from_file_location("hidden_4", path_to_pyc)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Get all names defined in the module that don't start with '__'
    names = [name for name in dir(hidden_4) if not name.startswith("__")]

    # Sort and print the names
    for name in sorted(names):
        print(name)
