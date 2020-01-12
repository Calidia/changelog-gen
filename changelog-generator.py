#!/usr/bin/env python3.7

from subprocess import PIPE, run


def main():
    logs = run(["git", "log", "--pretty=format:\"%cn - %cd - %s\""], capture_output=True, text=True)
    logs = logs.stdout.replace("\"", "").split("\n")

    formatted_logs = {"uncategorized": []}

    for log in logs:
        if "feature:" in log:
            if "features" in formatted_logs:
                print(formatted_logs)
                formatted_logs["features"].append(log)
            else:
                formatted_logs["features"] = [log]
        elif "chore:" in log:
            if "chore" in formatted_logs:
                formatted_logs["chore"].append(log)
            else:
                formatted_logs["chore"] = [log]
        elif "docs:" in log:
            if "docs" in formatted_logs:
                formatted_logs["docs"].append(log)
            else:
                formatted_logs["docs"] = [log]
        elif "fix:" in log:
            if "fix" in formatted_logs:
                formatted_logs["fix"].append(log)
            else:
                formatted_logs["fix"] = [log]
        elif "refactor:" in log:
            if "refactor" in formatted_logs:
                formatted_logs["refactor"].append(log)
            else:
                formatted_logs["refactor"] = [log]
        elif "test:" in log:
            if "test" in formatted_logs:
                formatted_logs["test"].append(log)
            else:
                formatted_logs["test"] = [log]
        else:
            formatted_logs["uncategorized"].append(log)

    print("The logs are:\n", formatted_logs)


if __name__== "__main__":
    main()