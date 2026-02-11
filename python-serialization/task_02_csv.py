#!/usr/bin/env python3
"""
Module to convert CSV data to JSON format
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV file to JSON format and save to data.json

    Args:
        csv_filename: name of the CSV file to convert

    Returns:
        True if conversion was successful, False otherwise
    """
    try:
        # Read CSV file
        data = []
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        # Write to JSON file
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found")
        return False
    except Exception as e:
        print(f"Error during conversion: {e}")
        return False
