"""
Experiment 09 - Convert CSV data to JSON format (CO-3)
Read data from a CSV file, convert it to JSON and write it to a .json file.
"""
import csv
import json
import os

csv_file = "students.csv"
json_file = "students.json"

# Create a sample CSV file if it does not exist
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["roll_no", "name", "branch", "marks"])
        writer.writerow([1, "Varad", "CSE", 92])
        writer.writerow([2, "Ansh", "CSE", 85])
        writer.writerow([3, "Malhar", "IT", 78])

# Read CSV into a list of dictionaries
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]

print("Data read from CSV:")
for row in data:
    print(row)

# Write JSON file
with open(json_file, "w") as f:
    json.dump(data, f, indent=4)

print(f"\nJSON data written to '{json_file}':")
with open(json_file, "r") as f:
    print(f.read())
