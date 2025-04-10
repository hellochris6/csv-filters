import csv
import re

input_file = "#"
output_file = "#"

# File extensions to include (lowercase)
include_extensions = (".heic", ".prproj", ".aae", ".xls", ".hprj", ".jpeg", ".mpeg", ".xmp")
#".mp4", ".mp3", ".mov", ".pdf", ".png", ".jpg", ".wav", 

with open(input_file, mode="r", newline="") as infile, open(output_file, mode="w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        if len(row) >= 2:
            col2 = row[1].strip().lower()
            if not col2.endswith(include_extensions):
                continue  # Skip rows that don't match
            # Write only columns 1 and 2
            writer.writerow([row[0], row[1]])
