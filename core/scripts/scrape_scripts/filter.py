import re

def remove(f_name):
    fp = open(f_name,"r+")
    for line in fp:
        if not re.search(r'\(\d+\)',line):
            fp.write(line)
remove("test.txt")
