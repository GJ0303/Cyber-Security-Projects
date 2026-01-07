import os
from datetime import datetime

def get_metadata(path):
    stats = os.stat(path)

    print("File:", path)
    print("Size:", stats.st_size, "bytes")
    print("Created:", datetime.fromtimestamp(stats.st_ctime))
    print("Modified:", datetime.fromtimestamp(stats.st_mtime))

file = input("Enter file path: ")
get_metadata(file)
