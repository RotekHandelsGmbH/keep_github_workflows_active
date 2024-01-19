# STDLIB
import json
import os
import pathlib
import sys
from typing import List, Dict
import urllib.request
from urllib.error import HTTPError
from urllib.parse import quote

# OWN
import lib_log_utils
import lib_detect_testenv

# CONFIG
if lib_detect_testenv.is_testenv_active():
    if os.getenv('GITHUB_ACTION'):
        owner = os.getenv('SECRET_GITHUB_OWNER')
        github_token = os.getenv('SECRET_GITHUB_TOKEN')
    else:
        config_directory = pathlib.Path("/rotek/scripts/credentials").absolute()
        sys.path.append(str(config_directory))
        from github_credentials import github_token, owner  # noqa


def enable_all_workflows(owner: str, github_token: str):
    """
    :param owner:
    :param github_token:
    :return:

    >>> # Test OK
    >>> enable_all_workflows(owner=owner, github_token=github_token)

    >>> # unknown owner
    >>> enable_all_workflows(owner='unknown_owner', github_token=github_token)
    Traceback (most recent call last):
        ...
    RuntimeError: ERROR reading repositories for user unknown_owner: Not Found


    >>> # wrong credentials
    >>> enable_all_workflows(owner=owner, github_token='invalid_credentials')
    Traceback (most recent call last):
        ...
    RuntimeError: ERROR reading repositories for user bitranox: Bad credentials

    """
    repositories = get_repositories(owner=owner, github_token=github_token)
    for repository in repositories:
        workflows = get_workflows(owner=owner, repository=repository, github_token=github_token)
        for workflow_filename in workflows:
            enable_workflow(owner=owner, repository=repository, workflow_filename=workflow_filename, github_token=github_token)


def get_repositories(owner: str, github_token: str) -> List[str]:
    """
    :param owner:   the username of the repository owner
    :param github_token:
    :return:

    >>> # Test Ok
    >>> get_repositories('bitranox', github_token)
    ['...', ..., '...']

    >>> # Test user not existing
    >>> get_repositories('user_does_not_exist', github_token)
    Traceback (most recent call last):
        ...
    RuntimeError: ERROR reading repositories for user user_does_not_exist: Not Found

    >>> # Test token not valid
    >>> get_repositories('bitranox', 'invalid_token')
    Traceback (most recent call last):
        ...
    RuntimeError: ERROR reading repositories for user bitranox: Bad credentials


    """
    url = f"https://api.github.com/users/{owner}/repos"
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    l_repositories: List[str]
    try:
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request) as response:
            data = response.read().decode("utf-8")
            l_dict_repositories: List[Dict[str, str]] = json.loads(data)
        l_repositories = [my_dict['name'] for my_dict in l_dict_repositories]
        result = f'found {len(l_repositories)} repositories for user {owner}'
        lib_log_utils.log_info(result)
    except HTTPError as exc:
        result_json = json.loads(exc.read().decode("utf-8"))
        result_error_message = result_json.get("message", "Error")
        result = f'ERROR reading repositories for user {owner}: {result_error_message}'
        lib_log_utils.log_error(result)
        raise RuntimeError(result)
    return l_repositories


def get_workflows(owner: str, repository: str, github_token: str) -> List[str]:
    """
    :param owner:   the username of the repository owner
    :param repository:
    :param github_token:
    :return:

    >>> # Setup
    >>> my_owner = 'bitranox'
    >>> l_repositories = get_repositories(owner=my_owner, github_token=github_token)

    >>> # Test OK
    >>> for my_repository in l_repositories:
    ...     get_workflows(owner=my_owner, repository=my_repository, github_token=github_token)
    [...]
    ...

    >>> # wrong owner
    >>> get_workflows(owner='does_not_exist', repository=l_repositories[0], github_token=github_token)
    Traceback (most recent call last):
        ...
    RuntimeError: ERROR reading repositories for user does_not_exist: Not Found

    >>> # wrong repository
    >>> get_workflows(owner='bitranox', repository='unknown_repository', github_token=github_token)
    Traceback (most recent call last):
        ...
    RuntimeError: ERROR reading repositories for user bitranox: Not Found

    >>> # token not valid
    >>> get_workflows(owner='bitranox', repository=l_repositories[0], github_token='invalid_token')
    Traceback (most recent call last):
        ...
    RuntimeError: ERROR reading repositories for user bitranox: Bad credentials

    """
    url = f"https://api.github.com/repos/{owner}/{repository}/actions/workflows"
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        # Make the API request
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request) as response:
            data = response.read().decode("utf-8")
            dict_workflows = json.loads(data)
            l_dict_workflows = dict_workflows['workflows']
            l_workflows = [pathlib.PosixPath(my_dict['path']).name for my_dict in l_dict_workflows]
        result = f'found {len(l_dict_workflows)} repositories for user {owner}, repository {repository}'
        lib_log_utils.log_info(result)

    except HTTPError as exc:
        result_json = json.loads(exc.read().decode("utf-8"))
        result_error_message = result_json.get("message", "Error")
        result = f'ERROR reading repositories for user {owner}: {result_error_message}'
        lib_log_utils.log_error(result)
        raise RuntimeError(result)
    return l_workflows


def enable_workflow(owner: str, repository: str, workflow_filename: str, github_token: str) -> str:
    """
    :param owner:               the username of the repository owner
    :param repository:          the name of the repository
    :param workflow_filename:   the name of the workflow for instance "python-package.yml"
    :param github_token:        the gitHub access token which has permission to perform the desired action

    >>> # Test OK
    >>> enable_workflow(owner=owner, repository="lib_path", workflow_filename="python-package.yml", github_token=github_token)
    'enabled repository lib_path, workflow python-package.yml'

    >>> # wrong owner
    >>> enable_workflow(owner='owner_does_not_exist', repository="lib_path", workflow_filename="python-package.yml", github_token=github_token)
    Traceback (most recent call last):
        ...
    RuntimeError: ERROR enabling repository lib_path, workflow python-package.yml: Not Found

    >>> # wrong repo
    >>> enable_workflow(owner=owner, repository="repo_does_not_exist", workflow_filename="python-package.yml", github_token=github_token)
    Traceback (most recent call last):
        ...
    RuntimeError: ERROR enabling repository repo_does_not_exist, workflow python-package.yml: Not Found


    >>> # wrong workflow
    >>> enable_workflow(owner=owner, repository="lib_path", workflow_filename="workflow_does_not_exist", github_token="wrong_credentials")
    Traceback (most recent call last):
        ...
    RuntimeError: ERROR enabling repository lib_path, workflow workflow_does_not_exist: Bad credentials


    """

    # API endpoint UR
    url = f"https://api.github.com/repos/{owner}/{repository}/actions/workflows/{quote(workflow_filename)}/enable"

    # Request headers
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {github_token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    # Prepare the request
    request = urllib.request.Request(url, headers=headers, method="PUT")
    try:
        urllib.request.urlopen(request)
        result = f'enabled repository {repository}, workflow {workflow_filename}'
        lib_log_utils.log_info(result)

    except HTTPError as exc:
        result_json = json.loads(exc.read().decode("utf-8"))
        result_error_message = result_json.get("message", "Error")
        result = f'ERROR enabling repository {repository}, workflow {workflow_filename}: {result_error_message}'
        raise RuntimeError(result)

    return result


# main{{{
def main() -> None:
    """
    enable all workflows in all repositories for the given owner
    >>> main()

    """
    # main}}}

    enable_all_workflows(owner=owner, github_token=github_token)


if __name__ == '__main__':
    print(b'this is a library only, the executable is named "keep_github_workflows_active_cli.py"', file=sys.stderr)
