import datetime


class SubmissionTrackerAgent:
    """
    A prototype agent that tracks submission status and deadlines.
    """
    def get_mock_tracking(self) -> list:
        """
        Return a list of mock submission tracking entries.

        :return: A list of dictionaries containing submission tracking information.
        """
        today = datetime.date.today()
        return [
            {
                "grant_id": "USDA-2025-AGR-112",
                "title": "USDA Urban Agriculture Innovation Grant",
                "application_status": "Draft",
                "deadlines": {
                    "internal_review": str(today.replace(month=today.month + 1, day=1)),
                    "final_submission": str(today.replace(month=today.month + 1, day=15)),
                },
                "reminders": [
                    f"{today.replace(month=today.month + 1, day=5)}: Internal review check",
                    f"{today.replace(month=today.month + 1, day=12)}: Final submission prep",
                ],
                "history_log": [
                    {"date": str(today), "event": "Draft v1 created"},
                ],
            }
        ]
