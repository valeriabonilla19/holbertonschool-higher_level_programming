#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
then saves them to a file in JSON format.
"""

import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing list if file exists, else start with an empty list
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Extend the list with command-line arguments (excluding script name)
items.extend(sys.argv[1:])

# Save updated list to the file
save_to_json_file(items, filename)
