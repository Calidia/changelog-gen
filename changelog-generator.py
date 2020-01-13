from subprocess import run
import os


def check_input(directory):
    try:
        os.chdir(directory)
        return True
    except:
        print("The directory does not exist")
        return False


def categorize_logs():
    logs = run(["git", "log", "--pretty=format:\"\u2022 %cn - %cr \n\tCommit - %s\"---"], capture_output=True, text=True)
    if "not a git repository" in logs.stderr:
        print("This directory does not contain a git repository")
        return False

    logs = logs.stdout.replace("\"", "").split("---")

    formatted_logs = {"uncategorized": []}

    for log in logs:
        if "feature:" in log:
            if "features" in formatted_logs:
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

    return formatted_logs


def create_changelog(logs):
    f = open("CHANGELOG.md", "w+")
    if logs:
        for section in logs.items():
            f.write(str(section[0] + ":\n").capitalize())
            commits = section[1:][0]
            for commit in commits:
                f.write("\t" + str(commit) + "\n")
            f.write("\n")
    f.close()


def main():
    while True:
        try:
            directory = input("Please enter the repository directory to generate a change log in: ")
        except:
            print("Sorry, didn't catch that.")
            continue

        if check_input(directory):
            logs = categorize_logs()
            if logs:
                create_changelog(logs)
                print("Change log was successfully generated in directory - ", os.getcwd().split("\\")[-1])
            break


if __name__== "__main__":
    main()