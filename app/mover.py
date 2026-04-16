import os
import shutil

def ensure_category_folder(base_directory, category):
    category_path = os.path.join(base_directory, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)
    return category_path

def get_unique_destination_path(destination_path):
    if not os.path.exists(destination_path):
        return destination_path
    base, ext = os.path.splitext(destination_path)
    counter = 1
    while True:
        new_destination = f"{base}_{counter}{ext}"
        if not os.path.exists(new_destination):
            return new_destination
        counter += 1

def move_file_to_category(file_path, base_directory, category):
    category_folder = ensure_category_folder(base_directory, category)
    destination_path = os.path.join(category_folder, os.path.basename(file_path))
    unique_destination = get_unique_destination_path(destination_path)
    shutil.move(file_path, unique_destination)