#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, "w+", "utf-8") as f:
        f.write(text)
