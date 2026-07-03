from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

from models.findings import ReviewFinding


class ReviewStatistics(BaseModel):
    """
    Review statistics.
    """

    total_findings: int = 0
    critical: int = 0
    high: int = 0
    medium: int = 0
    low: int = 0


class ReviewSummary(BaseModel):
    """
    Final synthesized review summary.
    """

    overall_score: int = Field(ge=0, le=100)

    summary: str

    strengths: List[str] = Field(default_factory=list)

    improvements: List[str] = Field(default_factory=list)


class ReviewResult(BaseModel):
    """
    Final review returned by the synthesizer.
    """

    pull_request_number: int

    repository: str

    generated_at: datetime

    statistics: ReviewStatistics

    summary: ReviewSummary

    findings: List[ReviewFinding] = Field(default_factory=list)