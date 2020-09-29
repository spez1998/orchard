#!/usr/bin/env python3

import sys
import toml
# Load user config
usr_config = toml.load("../config/test_config.toml")
# Load in-use config
current_config = toml.load("output.toml")              
# Check if requested module exists in config
if sys.argv[1] in usr_config.keys():                    
    module = sys.argv[1]
else:
    print("Module not specified in config.toml")
    exit()

count = 1 # Change this for something more functional
current_submodule = current_config.get(module)
# Get next submodule down from config list
req_submodule = usr_config.get(module).get(str(count))
print(current_submodule)
print(req_submodule)
while True:
    # Wait for user toggle
    input("Press Enter to toggle module behaviour\n")
    # Check if currently displayed module is the same as first in user config
    #if current_submodule == req_submodule:
    #    count += 1
    #print(usr_config)
    count += 1
    if current_submodule == req_submodule:
        count += 1
    req_submodule = usr_config.get(module).get(str(count))
    #print(req_submodule)
    current_config[module] = req_submodule
    #print(current_config)
    with open('output.toml', "w") as toml_file:
        toml.dump(current_config,toml_file)
        # Print next submodule down in TOML format
    ##########print(to_dump := "[{}]\n{}".format(module,toml.dumps(req_submodule)))
    # print(to_dump_dict := {'['module']': {'path': toml.dumps(req_submodule), 'reload': '1'}}
    #toml.dump(to_dump,"./output.toml")
    # print(usr_config[module])
    print(count)
