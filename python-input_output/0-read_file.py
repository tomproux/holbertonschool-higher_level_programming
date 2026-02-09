#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, "r", "utf-8") as f:
        f.read()
