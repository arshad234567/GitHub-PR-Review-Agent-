from collections import Counter

from models.review import ReviewResult, ReviewSummary, ReviewStatistics
from models.findings import ReviewFinding


class SynthesisService:
    def generate_review(self, workflow_state) -> ReviewResult:
        findings: list[ReviewFinding] = []

        findings.extend(workflow_state.quality_findings)
        findings.extend(workflow_state.security_findings)
        findings.extend(workflow_state.style_findings)
        findings.extend(workflow_state.architecture_findings)

        findings = self._remove_duplicates(findings)

        statistics = self._build_statistics(findings)

        summary = ReviewSummary(
            summary=self._generate_summary(statistics),
            recommendation="COMMENT",
        )

        return ReviewResult(
            findings=findings,
            statistics=statistics,
            summary=summary,
        )

    def _remove_duplicates(
        self,
        findings: list[ReviewFinding],
    ) -> list[ReviewFinding]:
        unique = {}

        for finding in findings:
            key = (
                finding.file_path,
                finding.line_number,
                finding.message,
            )

            unique[key] = finding

        return list(unique.values())

    def _build_statistics(
        self,
        findings: list[ReviewFinding],
    ) -> ReviewStatistics:
        """
        Generates review statistics.
        """

        severity_counter = Counter(
            finding.severity.value
            for finding in findings
        )

        return ReviewStatistics(
            total_findings=len(findings),
            critical=severity_counter.get("critical", 0),
            high=severity_counter.get("high", 0),
            medium=severity_counter.get("medium", 0),
            low=severity_counter.get("low", 0),
        )

    def _generate_summary(
        self,
        statistics: ReviewStatistics,
    ) -> str:
        """
        Creates a human-readable review summary.
        """

        return (
            f"Found {statistics.total_findings} issues "
            f"({statistics.critical} critical, "
            f"{statistics.high} high, "
            f"{statistics.medium} medium, "
            f"{statistics.low} low)."
        )