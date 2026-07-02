from typing import Any

from github.PullRequest import PullRequest
from github.Repository import Repository

from Github.github_client import GitHubClient


class PullRequestFetcher:
    """
    Fetches pull request information
    from GitHub.
    """

    def __init__(self):
        self.github_client = GitHubClient()

    def get_repository(
        self,
        installation_id: int,
        repository_name: str,
    ) -> Repository:
        """
        Fetch repository object.
        """

        client = self.github_client.get_installation_client(
            installation_id
        )

        return client.get_repo(repository_name)

    def get_pull_request(
        self,
        installation_id: int,
        repository_name: str,
        pr_number: int,
    ) -> PullRequest:
        """
        Fetch pull request object.
        """

        repository = self.get_repository(
            installation_id,
            repository_name,
        )

        return repository.get_pull(pr_number)

    def get_changed_files(
        self,
        installation_id: int,
        repository_name: str,
        pr_number: int,
    ) -> list[Any]:
        """
        Returns changed files in the PR.
        """

        pr = self.get_pull_request(
            installation_id,
            repository_name,
            pr_number,
        )

        return list(pr.get_files())

    def get_commits(
        self,
        installation_id: int,
        repository_name: str,
        pr_number: int,
    ) -> list[Any]:
        """
        Returns commits in the PR.
        """

        pr = self.get_pull_request(
            installation_id,
            repository_name,
            pr_number,
        )

        return list(pr.get_commits())