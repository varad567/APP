"""
Experiment 08 - File handling (CO-3)
Read data from an input file, count lines, extract the first two lines
and write the extracted data into a new file.
"""
import os

input_file = "input.txt"
output_file = "output.txt"

# Create a sample input file if it does not exist
if not os.path.exists(input_file):
    with open(input_file, "w") as f:
        f.write("Python is a high-level programming language.\n")
        f.write("It supports object-oriented programming.\n")
        f.write("Python is widely used in AI and ML.\n")
        f.write("File handling is done using open().\n")

# Read file and count lines
with open(input_file, "r") as f:
    lines = f.readlines()

print("Total number of lines:", len(lines))

# Extract first two lines
first_two = lines[:2]
print("\nFirst two lines:")
for line in first_two:
    print(line.strip())

# Write extracted lines to a new file
with open(output_file, "w") as f:
    f.writelines(first_two)

print(f"\nExtracted data written to '{output_file}'")

# Verify
with open(output_file, "r") as f:
    print("\nContents of output file:")
    print(f.read())
