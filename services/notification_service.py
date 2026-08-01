from models.review import ReviewResult


class NotificationService:

    def __init__(self, review_poster):
        self.review_poster = review_poster

    def publish_review(
        self,
        installation_id: int,
        repository_name: str,
        pr_number: int,
        review: ReviewResult,
    ) -> None:
        self.review_poster.post_review(
            installation_id=installation_id,
            repository_name=repository_name,
            pr_number=pr_number,
            comments=review.findings,
            summary=review.summary.summary,
        )

    def publish_status(
        self,
        installation_id: int,
        repository_name: str,
        pr_number: int,
        status: str,
    ) -> None:
        self.review_poster.post_status(
            installation_id=installation_id,
            repository_name=repository_name,
            pr_number=pr_number,
            status=status,
        )