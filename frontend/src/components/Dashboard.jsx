import React from "react";

export default function Dashboard({ onBack }) {
  return (
    <div style={{ padding: 24 }}>
      <header style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <h1>AI Marketing Dashboard</h1>
        <button onClick={onBack}>Back</button>
      </header>

      <section style={{ marginTop: 24 }}>
        <h2>Agents</h2>
        <ul>
          <li>Cleaning Agent</li>
          <li>Sentiment Agent</li>
          <li>Trend Agent</li>
          <li>Forecast Agent</li>
        </ul>
      </section>

      <section style={{ marginTop: 24 }}>
        <h2>Quick Actions</h2>
        <p>Use the API endpoints to run agents and view results.</p>
      </section>
    </div>
  );
}
