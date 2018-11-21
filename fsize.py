#!/usr/local/bin/python3
import sys
import os
from humanize import naturalsize
from glob2 import iglob

# Check the length of the arguments.
if len(sys.argv) <= 1:
    print("usage: fsize /path/to/dir /path/to/file ...\ncalculates the size of files and directories and displays each in a human-readable format")
    exit(1)


def size(path:str):
    try:
        if os.path.isdir(path):
            return naturalsize(sum(os.path.getsize(fd) for fd in iglob('{}/**'.format(path))))
        else:
            return naturalsize(os.path.getsize(path))
    except:
        "Failed to calculate."

# Print size for each path
for path in sys.argv[1:]:
    print("{} \t {}".format(path, size(path)))