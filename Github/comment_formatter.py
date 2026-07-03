from typing import List

class CommentFormatter:
    """
    Formats review findings into GitHub review comments.
    """
    @staticmethod
    def format_single_comment(
        file_path: str,
        line_number: int,
        severity: str,
        category: str,
        message: str,
        suggestion: str | None = None,
    ) -> dict:
        """
        Format a single review comment.
        """

        body = (
            f"### {severity.upper()} | {category}\n\n"
            f"{message}"
        )

        if suggestion:
            body += f"\n\n**Suggestion:**\n{suggestion}"

        return {
            "path": file_path,
            "line": line_number,
            "body": body,
        }

    @staticmethod
    def format_review(
        findings: List[dict],
    ) -> List[dict]:
        """
        Format multiple review findings.
        """

        comments = []

        for finding in findings:

            comments.append(
                CommentFormatter.format_single_comment(
                    file_path=finding["file_path"],
                    line_number=finding["line"],
                    severity=finding["severity"],
                    category=finding["category"],
                    message=finding["message"],
                    suggestion=finding.get("suggestion"),
                )
            )

        return comments





#After formatting:

# {
#     "path": "app/auth.py",
#     "line": 42,
#     "body": """### HIGH | Security
#
# Potential SQL Injection detected.
#
# **Suggestion:**
# Use parameterized queries instead.
# """
# }


