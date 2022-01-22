# Python.Python imports
import sys
import os
import glob

# My imports
from FileOperations import filesInDir

commandLineArguments = sys.argv
absolutePath = os.path.abspath(commandLineArguments[1])

f = open(absolutePath, "r+")

lines = []

for line in f.readlines():
    if line[:8] == "#include":
        line = line.strip("\n")
        lines.append(line)


print(filesInDir())

f.close()
