#!/usr/bin/env python3

import sys
import toml

usr_config = toml.load("../test_config.toml")

count = 1

if sys.argv[1] in usr_config.keys():
    module = sys.argv[1]
else:
    print("Module not specified in config.toml")
    exit()

count = 1
while True:
    input("Press Enter to toggle module behaviour\n")
    print(usr_config.get(module).get(str(count)))
    if count == 1:
        count += 1
    else:
        count = 1
