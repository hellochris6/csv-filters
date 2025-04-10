import csv
import re

input_file = "#"
output_file = "#"

# File extensions to exclude (lowercase)
exclude_extensions = (".mp4", ".mp3", ".mov", ".pdf", ".png", ".jpg", ".wav", ".heic", ".prproj", ".AAE", ".xls", ".hprj", ".jpeg", ".mpeg", ".xmp")

with open(input_file, mode="r", newline="") as infile, open(output_file, mode="w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        if len(row) >= 2:
            col2 = row[1].strip().lower()
            if col2.endswith(exclude_extensions):
                continue  # Skip the row
            # Keep only columns 1 and 2
            writer.writerow([row[0], row[1]])
