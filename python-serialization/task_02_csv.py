#!/usr/bin/env python3
"""reading data from one format (CSV) converting into another format (JSON) """

import csv
import json


def convert_csv_to_json(csv_filename):
    """convert cvs to json"""
    try:
        with open(csv_filename, 'r', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            data = [row for row in csv_reader]

        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False

    except Exception as e:
        print("Error:", e)
        return False
