# Bulk File Renamer

A lightweight Python utility that renames files in bulk using the current folder name as the filename prefix. The application is designed to work directly inside the target folder without requiring the user to browse for folders or enter file paths.

---

## Features

* Automatically uses the current folder name as the filename prefix.
* Renames files sequentially while preserving their original file extensions.
* Supports multiple sorting methods:

  * Name (A–Z)
  * Date Modified (Oldest First)
  * File Size (Smallest First)
* Safe two-phase renaming process to prevent filename conflicts.
* Optional file type filtering.
* Works with any file type.
* No external Python libraries required.
* Can be packaged into a standalone Windows executable using PyInstaller.

---

## How It Works

1. Copy **rename.exe** (or **rename.py**) into the folder containing the files you want to rename.
2. Run the application.
3. Select one of the available sorting methods:

   * Name
   * Date
   * Size
4. The application safely renames all matching files using the current folder name as the filename prefix.

---

## Example

### Before

```text
Holiday
│
├── IMG_1045.jpg
├── DSC_9812.jpg
├── Beach.png
├── Notes.txt
├── Video.mp4
```

### After

```text
Holiday
│
├── Holiday_001.jpg
├── Holiday_002.jpg
├── Holiday_003.png
├── Holiday_004.txt
├── Holiday_005.mp4
```

---

## Screenshots

### Application Poster

```markdown
!(screenshots/poster.png)
```

## Folder Structure

```text
Bulk-File-Renamer
│
├── rename.py
├── README.md
├── requirements.txt
├── .gitignore
├── screenshots
│   ├── poster.png
│   ├── before.png
│   └── after.png
└── Test_files
```

---

## Requirements

* Python 3.14 or later
* Windows 11 (Tested)
* No external Python packages required

---

## Technologies Used

* Python
* pathlib
* PyInstaller
* Git
* GitHub

---

## Console Output

```text
============================================================
Bulk File Renamer
============================================================

Target Folder : Holiday

Select Sorting Method

1. Name (A-Z)
2. Date (Oldest First)
3. Size (Smallest First)

Files Found : 24

Phase 1 - Creating Temporary Names

Phase 2 - Applying Final Names

============================================================
Summary
============================================================

Files Found    : 24
Files Renamed  : 24
Errors         : 0

Completed Successfully
```

---

## Future Enhancements

Potential future improvements include:

* Preview mode before renaming.
* Undo previous rename operation.
* Additional sorting options.
* Support for custom filename prefixes.
* Cross-platform compatibility enhancements.

---

## Author

**Ganesh DG**

GitHub: https://github.com/dg-ganesh

---

## License

This project is released under the MIT License.

screenshots/poster.png