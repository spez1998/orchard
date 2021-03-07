#!/usr/bin/env python3

import sys
import toml

usr_config = toml.load("../config/test_config.toml")
count = 1
arg = sys.argv[1].split(".")

if arg[0] in usr_config.keys():
    module = arg[0]
    submodule_num = arg[1]
else:
    print("Module not specified in config.toml")
    exit()

print(f"You are using date.{submodule_num}")

count = int(submodule_num) # Start at current submodule
while True:
    input("Press Enter to go to next module\n")
    num_variants = len(usr_config.get(module).keys())
    next_submodule_num = (count%num_variants)+1 # Get next number down, loop to top of list if at bottom
    submodule = dict(usr_config.get(module).get(str(next_submodule_num))) # Get next submodule down from config list
    print(f"[{module}]\n{toml.dumps(submodule)}")
    print(f"You are now using date.{next_submodule_num}")
    count += 1
