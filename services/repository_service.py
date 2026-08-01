from Github.pr_fetcher import PullRequestFetcher
from models.github import PullRequestInfo


class RepositoryService:

    def __init__(self, github_client):
        self.pr_fetcher = PullRequestFetcher(github_client)

    def fetch_pull_request(
        self,
        installation_id: int,
        repository_name: str,
        pr_number: int,
    ) -> PullRequestInfo:
        return self.pr_fetcher.fetch_pull_request(
            installation_id=installation_id,
            repository_name=repository_name,
            pr_number=pr_number,
        )

    def fetch_changed_files(
        self,
        installation_id: int,
        repository_name: str,
        pr_number: int,
    ):
        return self.pr_fetcher.fetch_changed_files(
            installation_id=installation_id,
            repository_name=repository_name,
            pr_number=pr_number,
        )

    def fetch_commits(
        self,
        installation_id: int,
        repository_name: str,
        pr_number: int,
    ):

        return self.pr_fetcher.fetch_commits(
            installation_id=installation_id,
            repository_name=repository_name,
            pr_number=pr_number,
        )

    def fetch_repository(
        self,
        installation_id: int,
        repository_name: str,
    ):

        return self.pr_fetcher.fetch_repository(
            installation_id=installation_id,
            repository_name=repository_name,
        )