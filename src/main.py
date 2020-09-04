#!/usr/bin/env python3

import sys
import toml

usr_config = toml.load("../config/test_config.toml") # Load user config into dict

count = 1

# Check if requested section exists in config
if sys.argv[1] in usr_config.keys():
    module = sys.argv[1]
else:
    print("Module not specified in config.toml")
    exit()

count = 1
print("Press Enter to toggle module behaviour\n")

#Toggling between different subsections
while True:
    input()
    submodule = usr_config.get(module).get(str(count)) # Get next submodule down from config list
    print(toml.dumps(submodule)) # Print next submodule down in TOML format
    # Keep iterating through submodules, loop back to top of list if bottom is reached
    if count == 1:
        count += 1
    else:
        count = 1
