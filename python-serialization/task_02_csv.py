#!/usr/bin/python3
"""
Module that converts CSV data to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts CSV data to JSON and writes to 'data.json'.

    Args:
        csv_filename (str): The path to the CSV file.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
