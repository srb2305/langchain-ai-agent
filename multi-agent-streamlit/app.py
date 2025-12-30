import streamlit as st
from dotenv import load_dotenv

from agents import (
    researcher_agent,
    analyst_agent,
    critic_agent,
    final_agent
)

load_dotenv()

st.set_page_config(page_title="Multi-Agent AI System", layout="wide")
st.title("🧠 Multi-Agent AI System (Day 9)")

st.markdown(
    """
This demo shows how **multiple AI agents collaborate** to answer one question.
Each agent has a specific responsibility — just like a real team.
"""
)

question = st.text_input("Ask a business question")

if st.button("Run Multi-Agent System"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Agents collaborating..."):

            st.subheader("🔍 Research Agent")
            research = researcher_agent(question)
            st.write(research)

            st.subheader("📊 Analyst Agent")
            analysis = analyst_agent(research, question)
            st.write(analysis)

            st.subheader("🧐 Critic Agent")
            critique = critic_agent(analysis)
            st.write(critique)

            st.subheader("✅ Final Agent (Answer)")
            final_answer = final_agent(research, analysis, critique)
            st.success(final_answer)
