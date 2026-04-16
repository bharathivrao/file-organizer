import os

FILE_CATEGORIES = {
    "Docs": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".csv", ".ppt", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
}

def get_category_for_file(file_name):
    for category, extensions in FILE_CATEGORIES.items():
        extension = os.path.splitext(file_name)[1].lower()
        if any(extension == ext for ext in extensions):
            return category
    return "Others"