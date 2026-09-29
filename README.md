# 🎓 University Admission AI

A beginner-friendly multi-agent university admission system built with CrewAI, Groq GPT-OSS 120B, and Streamlit.

## Agents

1. Requirements Agent
2. Eligibility Agent
3. Program Recommendation Agent

The workflow is sequential:

Requirements → Eligibility → Recommendation

There is no hierarchical process, manager agent, or delegation.

## Deploy without installing anything locally

1. Create a GitHub repository.
2. Upload these files.
3. Open Streamlit Community Cloud.
4. Connect the GitHub repository.
5. Select `app.py` as the main file.
6. Add your Groq API key to Streamlit Secrets.

Secret name:

`GROQ_API_KEY`

Example:

`GROQ_API_KEY = "your-groq-api-key"`

Never put the API key directly into Python files or commit it to GitHub.

## Important

The application currently expects the user to paste official university/program admission requirements.

This is an AI-assisted preliminary assessment and does not replace the university's official admission decision.
