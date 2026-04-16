# File Organizer Automation

A beginner-friendly Python automation project that organizes files in a directory based on file type. It can scan a folder once and move files into categorized folders, and it can also watch the folder in real time for new or modified files.

## Features

- Organizes files by extension into folders like:
  - Docs
  - Images
  - Videos
  - Audio
  - Archives
  - Others
- Creates category folders automatically if they do not exist
- Renames duplicate files safely to avoid overwriting
- Supports one-time organization of a directory
- Supports real-time monitoring using `watchdog`
- Ignores hidden files like `.DS_Store`

## Project Structure

```text
file-organizer/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── cli.py
│   ├── rules.py
│   ├── scanner.py
│   ├── organizer.py
│   ├── mover.py
│   └── watcher.py
├── tests/
│   ├── test_rules.py
│   ├── test_mover.py
│   ├── test_organizer.py
│   └── test_watcher.py
├── sample_files/
├── .gitignore
├── README.md
├── requirements.txt
└── run.py

Tech Stack
	•	Python
	•	os
	•	shutil
	•	watchdog
	•	pytest

How It Works

The application:
	1.	scans a directory for files
	2.	determines the category of each file based on its extension
	3.	creates a matching destination folder if needed
	4.	moves the file into that folder
	5.	optionally watches the folder continuously for changes

Supported Categories

Examples of file organization rules:
	•	Docs: .pdf, .doc, .docx, .txt, .csv, .xlsx, .ppt, .pptx
	•	Images: .jpg, .jpeg, .png, .gif, .webp
	•	Videos: .mp4, .mov, .avi, .mkv
	•	Audio: .mp3, .wav, .aac
	•	Archives: .zip, .rar, .tar, .gz
	•	Others: any unrecognized extension

##Setup

1. Clone the repository

git clone https://github.com/bharathivrao/file-organizer
cd file-organizer


2. Create and activate a virtual environment

On macOS/Linux:
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

##Usage

Organize a directory once:

python run.py --path "./sample_files"

Watch a directory in real time:

python run.py --path "./sample_files" --watch

##Example

Suppose your folder contains:
sample_files/
├── resume.pdf
├── photo.jpg
├── notes.txt
├── movie.mp4
└── archive.zip

After running the organizer, it becomes:

sample_files/
├── Docs/
│   ├── resume.pdf
│   └── notes.txt
├── Images/
│   └── photo.jpg
├── Videos/
│   └── movie.mp4
└── Archives/
    └── archive.zip
	
	
##Duplicate File Handling

If a file with the same name already exists in the destination folder, the program renames the new file instead of overwriting it.

Example:

resume.pdf
resume_1.pdf
resume_2.pdf

##Running Tests

Run all tests:

pytest

If you get import issues locally, run:

PYTHONPATH=. pytest

##Test Coverage

The project includes tests for:
	•	file type categorization
	•	safe file moving
	•	organizing directories
	•	watcher helper behavior

##Future Improvements
	•	Add custom user-defined rules
	•	Add recursive subfolder organization
	•	Add logging to a file
	•	Add support for ignoring specific filenames or extensions
	•	Package as a background service
	•	Add config file support using JSON or YAML

##What I Learned

This project helped me practice:
	•	file and directory handling in Python
	•	working with os and shutil
	•	event-driven programming with watchdog
	•	safe handling of duplicate filenames
	•	writing tests with pytest

##License

This project is for learning and portfolio purposes.


