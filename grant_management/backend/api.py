from flask import Flask, jsonify, request
from agents.opportunity_finder import OpportunityFinderAgent
from agents.submission_tracker import SubmissionTrackerAgent
from agents.grant_writer import GrantWriterAgent
from agents.reviewer_insight import ReviewerInsightAgent



def create_app() -> Flask:
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)

    @app.route("/api/opportunities", methods=["GET"])
    def get_opportunities():
        agent = OpportunityFinderAgent()
        data = agent.fetch_mock_opportunities()
        return jsonify(data)

    @app.route("/api/submissions", methods=["GET"])
    def get_submissions():
        agent = SubmissionTrackerAgent()
        data = agent.get_mock_tracking()
        return jsonify(data)

    @app.route("/api/draft", methods=["POST"])
    def generate_draft():
        """
        Generate a draft proposal given an opportunity and organization profile.
        Expects JSON body with 'opportunity' and 'org_profile' objects.
        """
        payload = request.get_json() or {}
        opportunity = payload.get("opportunity", {})
        org_profile = payload.get("org_profile", {})
        agent = GrantWriterAgent()
        draft = agent.generate_draft(opportunity, org_profile)
        return jsonify(draft)

    @app.route("/api/reviewer_insights", methods=["GET"])
    def get_reviewer_insights():
        """
        Provide reviewer priorities and suggestions.
        """
        agent = ReviewerInsightAgent()
        insights = agent.get_mock_insights()
        return jsonify(insights)

    return app


if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run(host="0.0.0.0", port=5000, debug=True)
