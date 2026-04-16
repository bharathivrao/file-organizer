import os

def get_files_in_directory(directory):
    if not os.path.exists(directory) or not os.path.isdir(directory):
        return []
    with os.scandir(directory) as entries:
        return [entry for entry in entries if entry.is_file()]