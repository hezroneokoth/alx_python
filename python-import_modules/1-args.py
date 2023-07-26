#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1

    if argc == 0:
        print("0 arguments."format(argc))
    elif argc == 1:
        print("1 argument:"format(argc))
    else:
        print("{} arguments:".format(argc))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
