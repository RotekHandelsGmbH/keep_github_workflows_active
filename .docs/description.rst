GitHub Workflow Management Script
==================================

This manual guides you through the execution of a Python script designed to manage GitHub workflows across all repositories of a user. The script performs two main functions:

1. **Keep All Workflows Active**: Ensures that all workflows in each repository of the user remain in an active state.

2. **Delete Old Workflow Runs**: For each repository, this function retains a specified number of the most recent workflow runs and deletes all older runs.


Access Key
-----------

In order to access the repository workflows, you will need a fine-grained personal test token. Follow the link to generate the token:

- [Generate Fine-Grained Personal Test Token](https://github.com/settings/personal-access-tokens)

Permissions
~~~~~~~~~~~

Ensure the access key has the following permissions:

- Action: Read/Write
- Metadata: Read

Test Token Details
------------------

The current test token is valid until 2025-01-19 and needs to be renewed annually.


Token Storage for testing
-------------------------

The token is stored as a secret in the repository's "repository secrets." Navigate to the following link to manage repository secrets:

- [Repository Secrets](https://github.com/bitranox/keep_github_workflows_active/settings/secrets/actions)

Secrets Information
~~~~~~~~~~~~~~~~~~~

The following secrets need to be set:

- `SECRET_GITHUB_OWNER`: the GitHub username
- `SECRET_GITHUB_TOKEN`: The fine-grained access key
