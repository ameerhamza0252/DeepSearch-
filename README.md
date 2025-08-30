# Deep Research System

**Deep Research System** is an AI-powered research framework that orchestrates multiple specialized agents to perform deep, multi-step research. It leverages OpenAI’s SDK, the Gemini API, and OpenAI Tracing to manage, track, and synthesize information efficiently. The system is designed to produce high-quality research reports with minimal human supervision.

---

## Features

* **Multi-Agent Architecture**: Specialized agents perform tasks such as fact-finding, source verification, planning, synthesis, and report writing.
* **Lead Researcher Agent**: Coordinates all research activities and ensures smooth workflow between agents.
* **Task Planning**: Breaks down complex research questions into manageable tasks.
* **Data Synthesis**: Combines research outputs into structured and organized insights.
* **Professional Report Generation**: Produces a polished and comprehensive research report.
* **Tracing and Logging**: Full traceability using OpenAI Tracing API; logs accessible on the OpenAI dashboard.
* **Gemini API Integration**: Leverages advanced language capabilities for research tasks.

---

## Repository Structure

| File                      | Description                                                     |
| ------------------------- | --------------------------------------------------------------- |
| `deep_research_system.py` | Main Lead Researcher agent coordinating all research.           |
| `research_agents.py`      | Specialist research agents (fact-finder, source-checker, etc.). |
| `planning_agent.py`       | Breaks complex questions into structured research tasks.        |
| `synthesis_agent.py`      | Combines research findings into organized insights.             |
| `report_writer.py`        | Generates the final professional research report.               |
| `Deep Research Demo.mp4`  | Demo video showing the system in action.                        |

---

## Getting Started

### Prerequisites

* Python 3.10+
* OpenAI Python SDK
* Gemini API Key
* OpenAI Tracing enabled for logs

### Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your environment variables:

```bash
export OPENAI_API_KEY="your-openai-api-key"
export GEMINI_API_KEY="your-gemini-api-key"
```

---

## Usage

Run the main Lead Researcher agent to start a research project:

```bash
python deep_research_system.py
```

* The planning agent will break down your research query into tasks.
* Specialist research agents will gather and verify information.
* The synthesis agent will organize the insights.
* The report writer agent will create the final report.
* Trace logs are available in the OpenAI dashboard for monitoring and debugging.

---

## Demo

A demo video showcasing the Deep Research System is included:

[Deep Research Demo.mp4](./Deep%20Research%20Demo.mp4)
