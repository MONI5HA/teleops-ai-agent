import { useState } from "react";
import {
  Activity,
  AlertTriangle,
  BrainCircuit,
  RadioTower,
  Wifi,
  Zap,
} from "lucide-react";

import { motion } from "framer-motion";
import "./App.css";

export default function App() {
  const [query, setQuery] = useState("");
  const [cellId, setCellId] = useState("NR-4402");
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);

  const handleAnalyze = async () => {
    setLoading(true);

    try {
      const res = await fetch("http://127.0.0.1:8000/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query, cell_id: cellId }),
      });

      const data = await res.json();
      setResponse(data);
    } catch (err) {
      console.error(err);
    }

    setLoading(false);
  };

  return (
    <div className="app">
      {/* glow background */}
      <div className="glow cyan" />
      <div className="glow purple" />

      <div className="container">

        {/* HEADER */}
        <motion.div className="header">
          <div className="header-left">
            <div className="icon-box cyan-border">
              <BrainCircuit className="icon cyan" />
            </div>

            <div>
              <h1 className="title">TeleOps AI Agent</h1>
              <p className="subtitle">
                Multi-Agent Telecom Intelligence Platform
              </p>
            </div>
          </div>
        </motion.div>

        <div className="grid">

          {/* LEFT PANEL */}
          <motion.div className="card left">
            <div className="card-title">
              <Zap className="icon cyan" />
              <h2>AI Network Analysis</h2>
            </div>

            <label>Cell ID</label>
            <input
              value={cellId}
              onChange={(e) => setCellId(e.target.value)}
              placeholder="NR-4402"
            />

            <label>Telecom Query</label>
            <textarea
              rows={7}
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Cell NR-4402 is showing degraded SINR..."
            />

            <button onClick={handleAnalyze}>
              {loading ? "Analyzing..." : "Run AI Analysis"}
            </button>
          </motion.div>

          {/* RIGHT PANEL */}
          <div className="right">

            {/* DIAGNOSIS */}
            <motion.div className="card">
              <div className="card-title">
                <Activity className="icon green" />
                <h2>AI Diagnosis</h2>
              </div>

              <p className="text">
                {response?.diagnosis || "Awaiting telecom analysis..."}
              </p>
            </motion.div>

            {/* KPI */}
            <div className="kpi-grid">

              <motion.div className="kpi cyan-card">
                <p>SINR</p>
                <h3>{response?.observability?.kpi?.sinr || "--"}</h3>
                <Wifi className="kpi-icon cyan" />
              </motion.div>

              <motion.div className="kpi purple-card">
                <p>Throughput</p>
                <h3>{response?.observability?.kpi?.throughput || "--"}</h3>
                <RadioTower className="kpi-icon purple" />
              </motion.div>

            </div>

            {/* ALARMS */}
            <motion.div className="card red">
              <div className="card-title">
                <AlertTriangle className="icon red" />
                <h2>Active Alarms</h2>
              </div>

              {response?.observability?.alarms?.length ? (
                response.observability.alarms.map((alarm, i) => (
                  <div key={i} className="alarm">
                    <strong>{alarm.alarm}</strong>
                    <span>{alarm.severity}</span>
                  </div>
                ))
              ) : (
                <p>No active alarms</p>
              )}
            </motion.div>

            {/* KNOWLEDGE */}
            <motion.div className="card">
              <h2>📚 Telecom Knowledge Sources</h2>

              {response?.knowledge_sources?.map((s, i) => (
                <div key={i} className="source">
                  {s}
                </div>
              ))}
            </motion.div>

          </div>
        </div>
      </div>
    </div>
  );
}