import os
import magic
import gzip

file_check = magic.Magic(mime=True)

def walkdir(folder):
    #Walk through each files in a directory
    for dirpath, dirs, files in os.walk(folder):
        for filename in files:
            yield os.path.abspath(os.path.join(dirpath, filename))

def logfile_check(dir):
    for filepath in walkdir(dir):
        absolute_path, extension = os.path.splitext(filepath)
        if file_check.from_file(filepath) == "text/plain":
            open_file = open(filepath, "r")

        elif extension == ".gz":
            open_file = gzip.GzipFile(filepath, "r")
        else:
            print("Not a log file found at: " + filepath)

input_dir = input("Give an directory: ")
logfile_check(input_dir)