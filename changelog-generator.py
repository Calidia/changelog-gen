#!/usr/bin/env python3.7

from subprocess import PIPE, run

logs = run(["git", "log"], stdout=PIPE, stderr=PIPE, universal_newlines=True)
print("The logs are:\n", logs.stdout)