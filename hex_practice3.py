import binascii
import os

dir_input = input("Give directory input: ")
test_file = open("D:\Documents\gen_dict.txt", "w")
test_file.write("dic = {")
test_file.close()

def walkdir(folder):
    #Walk through each files in a directory
    for dirpath, dirs, files in os.walk(folder):
        for filename in files:
            yield os.path.abspath(os.path.join(dirpath, filename))

for filepath in walkdir(dir_input):
    filename, file_extension = os.path.splitext(filepath)
    with open(filepath, 'rb') as f:
        content = f.read()
    hex_var = str(binascii.hexlify(content))
    fh = open("D:\Documents\gen_dict.txt", "a")
    fh.write("\n  '" + file_extension + "' : '" + hex_var + "',")
    fh.close()

test2_file = open("D:\Documents\gen_dict.txt", "a")
test2_file.write("}")
test2_file.close()