from app.scanner import get_files_in_directory
from app.mover import move_file_to_category
from app.rules import get_category_for_file

def organize_directory(directory):
    files = get_files_in_directory(directory)
    if not files:
        print(f"No files found in directory '{directory}'.")
        return
    for file in files:
        category = get_category_for_file(file.name)
        move_file_to_category(file.path, directory, category)