from github.PullRequest import PullRequest

from Github.github_client import GitHubClient


class ReviewPoster:
    """
    Posts review comments and review summaries
    to GitHub Pull Requests.
    """

    def __init__(self):
        self.github_client = GitHubClient()

    def post_review(
        self,
        installation_id: int,
        repository_name: str,
        pr_number: int,
        comments: list[dict],
        summary: str,
        event: str = "COMMENT",
    ):
        """
        Post a pull request review.

        Supported events:
        - COMMENT
        - APPROVE
        - REQUEST_CHANGES
        """

        client = self.github_client.get_installation_client(
            installation_id
        )

        repository = client.get_repo(repository_name)

        pull_request: PullRequest = repository.get_pull(pr_number)

        review_comments = []

        for comment in comments:

            review_comments.append(
                {
                    "path": comment["path"],
                    "line": comment["line"],
                    "body": comment["body"],
                }
            )

        return pull_request.create_review(
            body=summary,
            event=event,
            comments=review_comments,
        )

    def approve(
        self,
        installation_id: int,
        repository_name: str,
        pr_number: int,
        summary: str,
    ):
        """
        Approve a pull request.
        """

        return self.post_review(
            installation_id=installation_id,
            repository_name=repository_name,
            pr_number=pr_number,
            comments=[],
            summary=summary,
            event="APPROVE",
        )

    def request_changes(
        self,
        installation_id: int,
        repository_name: str,
        pr_number: int,
        comments: list[dict],
        summary: str,
    ):
        """
        Request changes on a pull request.
        """

        return self.post_review(
            installation_id=installation_id,
            repository_name=repository_name,
            pr_number=pr_number,
            comments=comments,
            summary=summary,
            event="REQUEST_CHANGES",
        )