import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="File Organizer Automation")
    parser.add_argument("--path", required=True, help="Path to the directory to organize")
    parser.add_argument("--watch", action="store_true", help="Watch the directory for changes and organize in real-time")
    return parser.parse_args()