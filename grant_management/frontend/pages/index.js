import { useState, useEffect } from "react";

export default function Dashboard() {
  const [opportunities, setOpportunities] = useState([]);
  const [submissions, setSubmissions] = useState([]);
  const [draft, setDraft] = useState(null);
  const [insights, setInsights] = useState({});

  // Fetch initial data on mount
  useEffect(() => {
    fetch("/api/opportunities")
      .then((res) => res.json())
      .then(setOpportunities);

    fetch("/api/submissions")
      .then((res) => res.json())
      .then(setSubmissions);

    fetch("/api/reviewer_insights")
      .then((res) => res.json())
      .then(setInsights);
  }, []);

  // Handler to generate a draft for the first opportunity using a sample org profile
  const handleGenerateDraft = () => {
    const sampleOpp = opportunities[0] || {};
    const orgProfile = { name: "Example Org" };
    fetch("/api/draft", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ opportunity: sampleOpp, org_profile: orgProfile }),
    })
      .then((res) => res.json())
      .then(setDraft);
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Grant Management Dashboard</h1>

      <section style={{ marginTop: "2rem" }}>
        <h2>Opportunities</h2>
        <ul>
          {opportunities.map((opp) => (
            <li key={opp.id}>
              <strong>{opp.title}</strong> — {opp.source}
              <br />
              Deadline: {opp.deadline} | Funding: ${'${'}opp.funding_amount{'}'}
            </li>
          ))}
        </ul>
      </section>

      <section style={{ marginTop: "2rem" }}>
        <h2>Submissions</h2>
        <ul>
          {submissions.map((sub) => (
            <li key={sub.grant_id}>
              <strong>{sub.title}</strong> — {sub.application_status}
              <br />
              Final Submission: {sub.deadlines.final_submission}
              <br />
              Reminders: {sub.reminders.join(", ")}
            </li>
          ))}
        </ul>
      </section>

      <section style={{ marginTop: "2rem" }}>
        <h2>Reviewer Insights</h2>
        <p>Priorities: {insights.priorities?.join(", ")}</p>
        <p>Suggestions: {insights.suggestions?.join(", ")}</p>
      </section>

      <section style={{ marginTop: "2rem" }}>
        <h2>Draft Generator</h2>
        <button onClick={handleGenerateDraft}>Generate Draft</button>
        {draft && <pre>{JSON.stringify(draft, null, 2)}</pre>}
      </section>
    </div>
  );
}
