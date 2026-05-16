import { motion } from "framer-motion";

export default function Landing({ onEnter }) {
  return (
    <div style={{ minHeight: "100vh", background: "#07070f", display: "flex", alignItems: "center", justifyContent: "center" }}>
      <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} style={{ color: "white", textAlign: "center" }}>
        <h1 style={{ fontSize: 48, marginBottom: 8 }}>AI Marketing Intelligence Platform</h1>
        <p style={{ maxWidth: 600, margin: "0 auto 24px" }}>Autonomous marketing analyses using LLMs, BERTopic, PandasAI, and ChromaDB.</p>
        <button onClick={onEnter} style={{ padding: "12px 24px", borderRadius: 8 }}>Enter</button>
      </motion.div>
    </div>
  );
}
