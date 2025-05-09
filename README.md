# CSV Filters

This repo contains two simple Python scripts for filtering rows in a CSV file based on file extensions. It supports both exclusion and inclusion filters, helping users clean up or sort large datasets with minimal setup.

## Scripts

### `exclude-filter.py`

Removes rows from a CSV where the second column (typically a filename or path) ends with one of the specified excluded file extensions.

**Excluded extensions:**
`.mp4`, `.mp3`, `.mov`, `.pdf`, `.png`, `.jpg`, `.wav`, `.heic`, `.prproj`, `.AAE`, `.xls`, `.hprj`, `.jpeg`, `.mpeg`, `.xmp`

### `include-filter.py`

Keeps only rows where the second column ends with one of the specified **included** extensions.

**Included extensions:**
`.heic`, `.prproj`, `.aae`, `.xls`, `.hprj`, `.jpeg`, `.mpeg`, `.xmp`

## Requirements

- Python 3.x
- No external libraries required
