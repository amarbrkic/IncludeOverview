import os
from typing import Final

filetypes: Final = ["cpp", "cc", "c", "h", "hpp"]


def filesInDir(dir="../..") -> list:
    files = []
    for file in os.listdir(path=dir):
        if file.find(".") and len(file.split(".")) > 1:
            fileExtension = file.split(".")[1]
            if any(fileExtension == filetype for filetype in filetypes):
                files.append(file)
    return files
