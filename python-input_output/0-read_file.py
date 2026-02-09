#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, "r", "UTF-8") as f:
        f.read()
