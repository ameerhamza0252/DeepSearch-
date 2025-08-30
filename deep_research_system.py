import os
import asyncio
import streamlit as st
from planning_agent import planner_agent
from research_agents import research_agents
from synthesis_agent import synthesizer_agent
from report_writer import report_writer
from agents import Runner

from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
runner = Runner()  # Default max turns

async def orchestrate(question: str):
    # Step 1: Planner
    plan_result = await runner.run(planner_agent, f"Question: {question}\nReturn JSON only.")

    # Parse tasks
    import json
    try:
        tasks = json.loads(plan_result.final_output)
    except Exception:
        tasks = [plan_result.final_output]

    # Step 2: Research (specialist agents)
    research_results = []
    for agent in research_agents:
        for task in tasks:
            res = await runner.run(agent, f"Research this: {task}")
            research_results.append(res.final_output)

    # Step 3: Synthesize findings
    synthesis_result = await runner.run(
        synthesizer_agent,
        f"Combine research findings:\n{research_results}"
    )

    # Step 4: Create final report
    final_report = await runner.run(
        report_writer,
        f"Generate a professional research report based on:\n{synthesis_result.final_output}"
    )

    return final_report.final_output

# --------------------------
# Streamlit UI
# --------------------------
st.set_page_config(page_title="Deep Research System", page_icon="🔎", layout="wide")
st.title("Deep Research System")

question = st.text_input("Enter your research question:")

if st.button("Run Research") and question.strip():
    with st.spinner("Agents are working..."):
        final = asyncio.run(orchestrate(question.strip()))
    st.subheader("📌 Final Research Report")
    st.markdown(final)
