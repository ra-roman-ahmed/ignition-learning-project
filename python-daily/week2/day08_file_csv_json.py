"""
Day 08 - File I/O, CSV, JSON, and proper error handling.
Simulates exporting tag readings to CSV and JSON - similar to a
Power Chart export workflow.
"""

import csv
import json


def export_to_csv(readings, filepath):
    """Write a list of reading dicts to a CSV file."""
    try:
        with open(filepath, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["tag", "area", "value"])
            writer.writeheader()
            for reading in readings:
                writer.writerow(reading)
        print(f"CSV written: {filepath}")
    except PermissionError:
        print(f"Cannot write {filepath} - check if it's open in Excel.")


def export_to_json(readings, filepath):
    """Write the same data to a JSON file."""
    try:
        with open(filepath, "w") as f:
            json.dump(readings, f, indent=2)
        print(f"JSON written: {filepath}")
    except PermissionError:
        print(f"Cannot write {filepath} - check file permissions.")


def read_csv_report(filepath):
    """Read a CSV file back and return it as a list of dicts."""
    try:
        with open(filepath, "r") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        print(f"{filepath} not found - run the export first.")
        return []


def main():
    readings = [
        {"tag": "WWTP_FIT_101", "area": "WWTP", "value": 452.7},
        {"tag": "WWTP_FIT_102", "area": "WWTP", "value": 398.2},
        {"tag": "CLEARWELL_LIT_201", "area": "CLEARWELL", "value": 78.5},
    ]

    csv_path = "python-daily/week2/readings.csv"
    json_path = "python-daily/week2/readings.json"

    export_to_csv(readings, csv_path)
    export_to_json(readings, json_path)

    print("\n--- Reading the CSV back ---")
    rows = read_csv_report(csv_path)
    for row in rows:
        print(f"{row['tag']:<20} {row['area']:<12} {row['value']}")

    print("\n--- Testing error handling (missing file) ---")
    read_csv_report("python-daily/week2/does_not_exist.csv")


if __name__ == "__main__":
    main()