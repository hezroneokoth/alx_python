#!/usr/bin/python3
import sys
args = sys.argv[1:]
num_args = len(args)

if num_args == 0:
    print("0 args.")
else:
    print(f"{num_args} {'arg' if num_args == 1 else 'args'}:")
    for idx, arg in enumerate(args, 1):
        print(f"{idx}: {arg}")
