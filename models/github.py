from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class RepositoryInfo(BaseModel):
    """
    Repository metadata.
    """

    id: int
    name: str
    full_name: str
    owner: str
    default_branch: str
    private: bool


class ChangedFile(BaseModel):
    """
    Represents a file modified in a pull request.
    """

    filename: str
    status: str
    additions: int
    deletions: int
    changes: int
    patch: Optional[str] = None


class CommitInfo(BaseModel):
    """
    Represents a commit in a pull request.
    """

    sha: str
    message: str
    author: str


class PullRequestInfo(BaseModel):
    """
    Pull request metadata.
    """

    number: int
    title: str
    description: Optional[str] = None

    state: str

    author: str

    base_branch: str
    head_branch: str

    created_at: datetime
    updated_at: datetime

    repository: RepositoryInfo

    changed_files: List[ChangedFile] = Field(default_factory=list)

    commits: List[CommitInfo] = Field(default_factory=list)