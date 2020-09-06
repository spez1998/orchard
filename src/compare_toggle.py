#!/usr/bin/env python3

import sys
import toml
usr_config = toml.load("../config/test_config.toml")    # Load user config
current_config = toml.load("output.toml")               # Load in-use config

if sys.argv[1] in usr_config.keys():                    # Check if requested module exists in config
    module = sys.argv[1]
else:
    print("Module not specified in config.toml")
    exit()

count = 1
print("Press Enter to toggle module behaviour\n")
input()
submodule = usr_config.get(module).get(str(count))      # Get next submodule down from config list
print(f"[{module}]\n{toml.dumps(submodule)}")           # Print next submodule down in TOML format
