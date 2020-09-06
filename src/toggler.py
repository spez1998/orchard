#!/usr/bin/env python3

import sys
import toml

usr_config = toml.load("../config/test_config.toml")            # Load user config into dict
count = 1
if sys.argv[1] in usr_config.keys():                            # Check if requested module exists in config
    module = sys.argv[1]
else:
    print("Module not specified in config.toml")
    exit()

count = 1
print("Press Enter to toggle module behaviour\n")
while True:                                                     # Toggling between different subsections
    input()
    # print(usr_config.get())
    submodule = dict(usr_config.get(module).get(str(count)))    # Get next submodule down from config list
    print(f"[{module}]\n{toml.dumps(submodule)}")               # Print next submodule down in TOML format
    if count == 1:                                              # Keep looping through submodules
        count += 1
    else:
        count = 1
