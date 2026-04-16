import os
from time import sleep
from app.rules import get_category_for_file
from app.mover import move_file_to_category
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, directory):
        self.directory = directory

    def should_ignore_file(self, file_name):
        return file_name.startswith(".")

    def on_modified(self, event):
        if not event.is_directory:
            file_path = event.src_path
            file_name = os.path.basename(file_path)
            if self.should_ignore_file(file_name):
                return
            if not os.path.exists(file_path):
                return
            if not os.path.isfile(file_path):
                return
            category = get_category_for_file(file_name)
            move_file_to_category(file_path, self.directory, category)
            print(f"Moved '{file_name}' to category '{category}'")
           
def watch_directory(directory):
    eventhandler = FileChangeHandler(directory)
    observer = Observer()
    observer.schedule(eventhandler, path=directory, recursive=False)
    observer.start()
    print(f"Watching directory '{directory}' for changes...")
    try:
        while True:
            sleep(1)  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
        print("Stopped watching directory.")

    observer.join()