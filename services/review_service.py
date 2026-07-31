from models.review import ReviewResult

class ReviewService:
    """
    Orchestrates the complete pull request review workflow.
    """
    def __init__(
        self,
        repository_service,
        rag_service,
        workflow,
        synthesis_service,
        review_poster,
    ):
        self.repository_service = repository_service
        self.rag_service = rag_service
        self.workflow = workflow
        self.synthesis_service = synthesis_service
        self.review_poster = review_poster

    async def review_pull_request(
        self,
        installation_id: int,
        repository_name: str,
        pr_number: int,
    ) -> ReviewResult:
        """
        Executes the end-to-end pull request review workflow.
        """

        pull_request = self.repository_service.fetch_pull_request(
            installation_id,
            repository_name,
            pr_number,
        )

        repository_context = self.rag_service.retrieve_context(
            pull_request
        )
        workflow_state = self.workflow.run(
            pull_request,
            repository_context,
        )
        review = self.synthesis_service.generate_review(
            workflow_state
        )
        self.review_poster.post_review(
            installation_id=installation_id,
            repository_name=repository_name,
            pr_number=pr_number,
            comments=review.findings,
            summary=review.summary.summary,
        )

        return review