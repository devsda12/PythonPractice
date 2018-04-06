import os
import magic
import gzip

file_check = magic.Magic(mime=True)

def walkdir(folder):
    #Walk through each files in a directory
    for dirpath, dirs, files in os.walk(folder):
        for filename in files:
            yield os.path.abspath(os.path.join(dirpath, filename))

#Function that checks logfiles for content
def logfile_check(dir):
    failed_logins = []
    for filepath in walkdir(dir):
        absolute_path, extension = os.path.splitext(filepath)
        if file_check.from_file(filepath) == "text/plain":
            open_file = open(filepath, "r")
            read_file = open_file.readlines()
            for line in read_file:
                if "failed" in line and "login" in line:
                    failed_logins.append(line)

        elif file_check.from_file(filepath) == "application/x-gzip":
            open_file = gzip.open(filepath, "r")
            read_file = open_file.readlines()
            for line in read_file:
                if "failed" in str(line) and "login" in str(line):
                    failed_logins.append(line)

        else:
            print("Not a log file found at: " + filepath)
            continue
    return failed_logins
input_dir = input("Give an directory: ")
print(logfile_check(input_dir))