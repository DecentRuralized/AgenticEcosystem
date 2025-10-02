class ReviewerInsightAgent:
    """
    A prototype agent that provides tailored recommendations based on funder and reviewer profiles.
    """
    def __init__(self):
        pass

    def get_mock_insights(self) -> dict:
        """
        Return a mock set of reviewer insights.
        In a full implementation, this method would analyze funder histories and reviewer comments.

        :return: A dictionary containing reviewer priorities and tailoring suggestions.
        """
        priorities = [
            "Evidence-based outcomes",
            "Clear budget justification",
            "Sustainability after funding ends",
        ]
        suggestions = [
            "Use terms like 'data-driven' and 'scalable' throughout the proposal.",
            "Avoid vague statements; support claims with metrics and past results.",
            "Highlight long-term sustainability plans beyond the grant period.",
        ]
        return {"priorities": priorities, "suggestions": suggestions}
