#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, "a+", "utf-8") as f:
        f.append(text)
