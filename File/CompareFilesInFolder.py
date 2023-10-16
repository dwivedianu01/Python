'''
We can compare directories and files by using python module filecmp.
The cmp function compares the files and returns True if they appear identical otherwise False.

Syntax: filecmp.cmp(f1, f2, shallow)
Parameters:

f1: Name of one file
f2: Name of another file to be compared
shallow: With this, we set if we want to compare content or not.
'''
# Importing Libraries
import os
from pathlib import Path
from filecmp import cmp


def findDuplicatesFiles(path):
    # list of all documents
    DATA_DIR = Path(path)
    files = sorted(os.listdir(DATA_DIR))
    allDuplicateFiles = []
    response = []

    for file_name in files:
        is_duplicate = False
        for dup_name in allDuplicateFiles:
            is_duplicate = cmp(
                DATA_DIR / file_name,
                DATA_DIR / dup_name[0],
                shallow=False
            )
            if is_duplicate:
                dup_name.append(file_name)
                break

        if not is_duplicate:
            allDuplicateFiles.append([file_name])

    for file_p in allDuplicateFiles:
        if (len(file_p) > 1):
            response.append(file_p)

    return response


def moveFile(destination, source, file):
    src_path = os.path.join(source, file)
    dst_path = os.path.join(destination, file)
    os.rename(src_path, dst_path)


# Print results
# print(duplicateFiles)
if __name__ == '__main__':
    # findDuplicatesFiles('C:\Temp\ComapreFiles')
    source = 'C:\Personal\Son photos-20200321T063228Z-001\Son photos-20200321T063228Z-001\Son photos\9 Months'
    destination = 'C:\Temp\ComapreFiles\DuplicateFiles'
    allFiles = findDuplicatesFiles(source)
    for dup in allFiles:
        for k in dup:
            print(k)
            moveFile(source=source, destination=destination, file=k)
