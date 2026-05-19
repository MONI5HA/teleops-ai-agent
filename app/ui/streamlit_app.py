
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import streamlit as st
from app.graph.teleops_graph import teleops_graph

st.title("🚀 TeleOps AI Agent")

query = st.text_input("Enter your query")
cell_id = st.text_input("Enter Cell ID")

if st.button("Analyze"):

    result = teleops_graph.invoke({
        "query": query,
        "cell_id": cell_id
    })

    st.subheader("📊 Diagnosis")
    st.write(result["final_answer"])

    st.subheader("📡 KPI Data")
    st.json(result["kpi_data"])

    st.subheader("🚨 Alarms")
    st.json(result["alarms"])

    st.subheader("📚 Retrieved Knowledge")
    st.write(result["rag_results"])