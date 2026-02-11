#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves to a file"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Try to load existing list, or create empty list if file doesn't exist
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add all command-line arguments (except script name)
items.extend(sys.argv[1:])

# Save the updated list
save_to_json_file(items, filename)
