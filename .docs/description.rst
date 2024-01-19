To ensure the continuous activation of all workflows and prevent expiration, please follow the steps below:

Access Key
-----------

In order to access the repository workflows, you will need a fine-grained personal test token. Follow the link to generate the token:

- [Generate Fine-Grained Personal Test Token](https://github.com/settings/personal-access-tokens)

Permissions
~~~~~~~~~~~

Ensure the access key has the following permissions:

- Action: Read/Write
- Metadata: Read

Token Details
-------------

The current token is valid until 2025-01-19 and needs to be renewed annually.

Token Storage for testing
-------------------------

The token is stored as a secret in the repository's "repository secrets." Navigate to the following link to manage repository secrets:

- [Repository Secrets](https://github.com/bitranox/keep_github_workflows_active/settings/secrets/actions)

Secrets Information
~~~~~~~~~~~~~~~~~~~

The following secrets need to be set:

- `SECRET_GITHUB_OWNER`: the GitHub username
- `SECRET_GITHUB_TOKEN`: The fine-grained access key
