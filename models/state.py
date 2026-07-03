from typing import List, Optional

from pydantic import BaseModel, Field

from models.findings import ReviewFinding
from models.github import PullRequestInfo
from models.review import ReviewResult


class WorkflowState(BaseModel):
    """
    Shared state across the LangGraph workflow.
    """

    pull_request: PullRequestInfo

    repository_context: List[str] = Field(default_factory=list)

    quality_findings: List[ReviewFinding] = Field(default_factory=list)

    security_findings: List[ReviewFinding] = Field(default_factory=list)

    style_findings: List[ReviewFinding] = Field(default_factory=list)

    architecture_findings: List[ReviewFinding] = Field(default_factory=list)

    final_review: Optional[ReviewResult] = None