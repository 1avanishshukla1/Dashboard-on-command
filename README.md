# Autonomous Voice-Enabled LLM Data Explorer

A stateful, memory-driven LLM agent designed for autonomous dataset exploration and interactive analysis.

This project combines:

* Context-aware LLM orchestration
* Structured project memory management
* Dynamic dataset inspection
* Model-generated analysis execution
* Optional voice interaction layer

The system demonstrates how to build an application-level stateful agent on top of a stateless LLM API.

---

## Overview

LLM APIs are stateless by default.
This project builds a stateful architecture around them using three global memory layers:

* `conversation_history` → full structured chat history
* `project_context` → structured dataset and analysis metadata
* `summary_memory` → short rolling state summary

Each API request reconstructs the full context before sending it to the model.

This allows iterative reasoning and dataset exploration across multiple interactions.

---

## Key Features

### 1. Structured Memory System

The agent maintains structured state across interactions:

* Dataset metadata
* Column information
* Missing value summaries
* Analysis notes
* Conversation trace

This avoids repeatedly sending raw data while preserving analytical continuity.

---

### 2. Autonomous Dataset Exploration

The agent can:

* Inspect dataset structure (`head`, `info`)
* Identify numerical and categorical columns
* Detect missing values
* Generate visualizations (e.g., age vs heart disease)
* Update structured project memory dynamically

All extracted information is stored inside `project_context`.

---

### 3. Model-Driven Code Execution

When the assistant reply includes a fenced Python block:

```python
# example
summary_memory = "updated summary"
project_context.append({"note": "analysis completed"})
```

The system:

1. Extracts the first Python block
2. Executes it inside the global scope
3. Updates memory structures

This enables self-updating agent behavior.

Note: For production use, replace direct execution with a sandboxed execution layer.

---

### 4. Voice Interaction (Optional)

The `DashboardBot` class extends the base agent with:

* Speech-to-text using `speech_recognition`
* Text-to-speech using `pyttsx3`
* Continuous conversational loop
* Exit commands: `exit`, `quit`, `stop`

This allows voice-driven dataset exploration.

---

## Project Structure

```
.
├── src/
│   ├── bot_fixed.py
│   ├── dashboard_bot.py
│
├── data/
│   └── sample.csv
│
├── requirements.txt
├── README.md
```

---

## Installation

Create and activate a virtual environment:

Windows:

```
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Agent

Basic usage:

```python
from dashboard_bot import DashboardBot

bot = DashboardBot(
    api_key="YOUR_API_KEY",
    endpoint="YOUR_ENDPOINT",
    dataset_path="data/sample.csv"
)

bot.start_working()
```

You will be prompted to enable microphone input.

---

## Context Construction

Each API call constructs a message payload like:

```python
[
  {"role": "system", "content": system_context},
  {"role": "system", "content": f"Project context: {project_context}"},
  {"role": "system", "content": f"Summary memory: {summary_memory}"},
  *conversation_history
]
```

This ensures the model always sees:

* Global behavior rules
* Dataset state
* Conversation history
* Short-term memory summary

---

## Security Notice

The current implementation executes model-generated Python code directly using `exec()`.

This is not recommended for production systems.

Before deploying publicly:

* Implement a sandbox execution layer
* Restrict allowed modules
* Disable filesystem access
* Whitelist allowed actions

Never expose raw execution in a public environment.

---

## Design Philosophy

This project explores how to:

* Build a stateful agent on top of a stateless API
* Maintain structured internal memory
* Enable iterative analytical reasoning
* Combine LLM orchestration with voice interaction

It is an experimental architecture focused on advanced LLM-driven system design.

---

## Future Improvements

* Sandboxed execution engine
* Structured JSON action protocol
* Context compression layer
* Automated dataset ingestion
* Web dashboard interface
* Dockerized deployment

---

## Author

Independent experimental project focused on autonomous LLM memory systems and data exploration workflows.

