from dataclasses import dataclass
from typing import List

@dataclass
class DiffChunk:
    """
    Represents a single hunk (chunk) in a git diff.
    """
    header: str
    added_lines: List[str]
    removed_lines: List[str]

@dataclass
class ParsedDiff:
    """
    Represents a parsed file diff.
    """

    filename: str
    status: str
    additions: int
    deletions: int
    changes: int
    patch: str
    chunks: List[DiffChunk]


class DiffParser:
    """
    Parses GitHub pull request file patches into
    structured objects.
    """
    @staticmethod
    def parse_file(file) -> ParsedDiff:
        """
        Parse a GitHub PullRequestFile object.
        """

        patch = file.patch or ""
        chunks = DiffParser.parse_patch(patch)
        return ParsedDiff(
            filename=file.filename,
            status=file.status,
            additions=file.additions,
            deletions=file.deletions,
            changes=file.changes,
            patch=patch,
            chunks=chunks,
        )

    @staticmethod
    def parse_patch(patch: str) -> List[DiffChunk]:
        """
        Parse a git patch into diff chunks.
        """

        if not patch:
            return []

        chunks = []
        current_chunk = None
        for line in patch.splitlines():
            if line.startswith("@@"):
                if current_chunk:
                    chunks.append(current_chunk)
                current_chunk = DiffChunk(
                    header=line,
                    added_lines=[],
                    removed_lines=[],
                )
            elif current_chunk:
                if line.startswith("+") and not line.startswith("+++"):
                    current_chunk.added_lines.append(line[1:])
                elif line.startswith("-") and not line.startswith("---"):
                    current_chunk.removed_lines.append(line[1:])

        if current_chunk:
            chunks.append(current_chunk)
        return chunks