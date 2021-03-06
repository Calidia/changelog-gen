# changelog-gen
Changelog generator for git commit messages of a project

# Syntax:
<type>: <commit body>

## Supported Types:
**chore**: Non-production updates to codebase 
**docs**: Documentation only changes
**feature**: A new feature
**fix**: A bug fix
**refactor**: A code change that neither fixes a bug nor adds a feature
**test**: Adding missing tests or correcting existing tests

Any unsupported types will be categorized in the uncategorized section of the CHANGELOG.md document.

###### Examples:
refactor: Added categorize_logs function
feature: Added functionality to categorize the logs according to the supported types or adds them to an uncategorized section
fix: Added the logs as arrays in the dictionaries to be able to append more
docs: Added README.md with instructions and further details regarding the project

# Running Instructions 
The project requires Python 3.7 to run.

Put the file in the same directory as the repository folder and run "python changelog-generator.py" in cmd. Then you will be prompted to enter the repository's name which will generate a CHANGELOG.md file.

# Current Functionality

Takes in the repository name and generates a CHANGELOG.md file which contains the categorized commits in the repository.

# Future Functionality
**Versioning**
    The next step for this project would be to add versioning which would give a better breakdown of the commits in larger projects which have multiple production iterations.
**CHANGELOG.md Style**
    Improving the formatting of the CHANGELOG.md file would ensure better readability.
**Enhanced Syntax Handling**
    The syntax will be enriched to contain, capture and categorize a wider variety of details for each commit.

# Known Issues
**Buggy formatting of the CHANGELOG.md file**
    Currently there are some issues which cause the formatting of the CHANGELOG.md file to be off. There are extra elements from the split function usage which I have not been able to handle yet.

No other issues have been noted so far. Please do let me know if you stumble upon any.

# Technology Choices
Python was chosen for the implementation of this project. The reason is because Python is the second language which I am most comfortable with after Java and is also one which you use in your company's technology stack.

# Assessment Approach
Firstly, I evaluated the existing solutions referenced by you, namely Conventional Commits and gitmoji. Moreover, I researched other developed solutions which gave me a better idea of the scope of the project and potential approaches. Please find those in the Resources section below. Consequently, I implemented a script which ran the git log command with pretty formatting options to extract the commiter name, relative date and the commit body. Then, those were categorized according to the supported types. That is then passed to a function which writes the CHANGELOG.md file containing the categories and respective commits data. Later on I added functionality to request the repository folder from the user and exception handling as well.

## Resources
Conventional Commits:
    https://www.conventionalcommits.org/en/v1.0.0/#summary
    
Gitmoji:
    https://gitmoji.carloscuesta.me/
    
Angular documentation Guidelines:
    https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines
    
Changelog generator implementeed by jackyef in JavaScript:
    https://github.com/jackyef/changelog-generator
    
Github documentation for commit history output:
    https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History
