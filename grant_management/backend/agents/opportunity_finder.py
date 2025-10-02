import datetime


class OpportunityFinderAgent:
    """
    A prototype agent that provides a list of mock grant opportunities.
    """
    def fetch_mock_opportunities(self) -> list:
        """
        Return a list of mock opportunities for demonstration purposes.

        :return: A list of dictionaries representing grant opportunities.
        """
        today = datetime.date.today()
        return [
            {
                "id": "USDA-2025-AGR-112",
                "title": "USDA Urban Agriculture Innovation Grant",
                "deadline": str(today.replace(month=today.month + 1, day=15)),
                "funding_amount": 250000,
                "eligibility": "Non-profits, educational institutions",
                "focus_area": "Urban Agriculture",
                "source": "USDA",
                "score": 0.87,
            },
            {
                "id": "NIH-2025-HEALTH-09",
                "title": "NIH Community Health Research",
                "deadline": str(today.replace(month=today.month + 2, day=10)),
                "funding_amount": 500000,
                "eligibility": "Research institutions, healthcare NGOs",
                "focus_area": "Public Health",
                "source": "NIH",
                "score": 0.75,
            },
        ]
