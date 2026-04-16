from app.organizer import organize_directory
from app.cli import parse_args
from app.watcher import watch_directory

def main():
    args = parse_args()
    if args.watch:
        print("Real-time watching is not implemented yet. Organizing once.")
        watch_directory(args.path)
    else:
        organize_directory(args.path)