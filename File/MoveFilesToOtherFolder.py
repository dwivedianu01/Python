
# Importing Libraries
import os
from pathlib import Path


def moveFile(destination, source, file):
    src_path = os.path.join(source, file)
    dst_path = os.path.join(destination, file)
    os.rename(src_path, dst_path)


# Print results
# print(duplicateFiles)
if __name__ == '__main__':

    source = 'C:\Personal'
    destination = 'C:\Temp\ComapreFiles'
    allFiles = sorted(os.listdir(source))
    for file in allFiles:
        moveFile(source=source, destination=destination, file=file)
