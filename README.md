# changelog-gen
Changelog generator for git commit messages

# Syntax
<type>: <commit body>

###### Supported Types:
**chore**: Non-production updates to codebase 
**docs**: Documentation only changes
**feature**: A new feature
**fix**: A bug fix
**refactor**: A code change that neither fixes a bug nor adds a feature
**test**: Adding missing tests or correcting existing tests

###### Examples:
refactor: Added categorize_logs function
feature: Added functionality to categorize the logs according to the supported types or adds them to an uncategorized section
fix: Added the logs as arrays in the dictionaries to be able to append more