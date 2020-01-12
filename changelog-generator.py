#!/usr/bin/env python3.7

from subprocess import PIPE, run


def main():
    logs = run(["git", "log"], capture_output=True, text=True)
    print("The logs are:\n", logs.stdout)


if __name__== "__main__":
    main()