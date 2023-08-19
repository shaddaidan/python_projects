# start by importing all the libraries we need

import sys
import clipboard # i do not have this module installed
import json

# now for the actual codes

# data = clipboard.paste()

# print(data)

# to copy clipboard.copy('copied stuff')

# now to make the program runnable from the command line

def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

save_items("test.json", {"key": "value"})

if len(sys.argv) == 2:
    command - sys.argv[1]
    print(command)

    if command == "save":
        print("save")
    elif command == "load":
        print("load")
    elif command == "list":
        print("list")
    else:
        print("unknown command")

else:
    print("please pass exactly one command.")

