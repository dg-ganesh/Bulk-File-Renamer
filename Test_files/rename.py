from pathlib import Path
import sys
import uuid

# ==========================================================
# Bulk File Renamer
# Version 1.2
# ==========================================================

# ----------------------------------------------------------
# Configuration
# ----------------------------------------------------------

# Rename only these file types.
# Leave empty [] to rename ALL files.
FILE_TYPES = []

# Number padding
NUMBER_DIGITS = 3

# Temporary filename prefix
TEMP_PREFIX = "__TEMP__"


# ==========================================================
# Helper Functions
# ==========================================================

def get_target_folder() -> Path:
    """
    Returns the folder where this script/executable is located.
    """
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent

    return Path(__file__).parent


def get_sort_method() -> str:
    """
    Ask the user how files should be sorted.
    """

    print("\nSelect Sorting Method")
    print("---------------------")
    print("1. Name (A-Z)")
    print("2. Date (Oldest First)")
    print("3. Size (Smallest First)")

    choice = input("\nEnter your choice (1-3): ").strip()

    if choice == "1":
        return "name"

    elif choice == "2":
        return "date"

    elif choice == "3":
        return "size"

    print("\nInvalid choice.")
    print("Defaulting to Name sorting.\n")

    return "name"


def get_files(folder: Path, sort_by: str) -> list[Path]:
    """
    Returns files after filtering and sorting.
    """

    script_name = Path(__file__).name if "__file__" in globals() else ""
    exe_name = Path(sys.executable).name if getattr(sys, "frozen", False) else ""

    files = []

    for item in folder.iterdir():

        if not item.is_file():
            continue

        if item.name == script_name:
            continue

        if item.name == exe_name:
            continue

        if FILE_TYPES:
            if item.suffix.lower() not in [ext.lower() for ext in FILE_TYPES]:
                continue

        files.append(item)

    if sort_by == "date":
        files.sort(key=lambda file: file.stat().st_mtime)

    elif sort_by == "size":
        files.sort(key=lambda file: file.stat().st_size)

    else:
        files.sort(key=lambda file: file.name.lower())

    return files


def rename_files(folder: Path, files: list[Path]) -> tuple[int, int]:
    """
    Renames files safely using a temporary name first.
    """

    prefix = folder.name

    renamed = 0
    errors = 0

    temp_files = []

    print("\nPhase 1 - Creating Temporary Names")
    print("----------------------------------")

    for file in files:

        temp_name = f"{TEMP_PREFIX}_{uuid.uuid4().hex}{file.suffix}"
        temp_path = file.with_name(temp_name)

        try:
            file.rename(temp_path)
            temp_files.append(temp_path)

        except Exception as ex:
            print(f"Failed : {file.name}")
            print(f"Reason : {ex}")
            errors += 1

    print("Temporary renaming completed.")

    print("\nPhase 2 - Applying Final Names")
    print("------------------------------")

    for index, temp_file in enumerate(temp_files, start=1):

        final_name = (
            f"{prefix}_{index:0{NUMBER_DIGITS}d}{temp_file.suffix}"
        )

        final_path = temp_file.with_name(final_name)

        try:
            temp_file.rename(final_path)

            print(
                f"Renamed : {final_path.name}"
            )

            renamed += 1

        except Exception as ex:
            print(f"Failed : {temp_file.name}")
            print(f"Reason : {ex}")
            errors += 1

    return renamed, errors


# ==========================================================
# Main
# ==========================================================

def main():

    print("=" * 60)
    print("Bulk File Renamer")
    print("=" * 60)

    target_folder = get_target_folder()

    print(f"\nTarget Folder : {target_folder.name}")
    print(f"Location      : {target_folder}")

    sort_by = get_sort_method()

    files = get_files(target_folder, sort_by)

    if not files:
        print("\nNo matching files found.")
        print("\nCompleted Successfully")
        return

    print(f"\nSorting By : {sort_by.title()}")
    print(f"Files Found: {len(files)}")

    if FILE_TYPES:
        print(f"File Types : {', '.join(FILE_TYPES)}")
    else:
        print("File Types : ALL")

    renamed, errors = rename_files(target_folder, files)

    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Files Found    : {len(files)}")
    print(f"Files Renamed  : {renamed}")
    print(f"Errors         : {errors}")

    print("\nCompleted Successfully")
    print("\nPress Enter to exit...")
    input()


if __name__ == "__main__":
    main()