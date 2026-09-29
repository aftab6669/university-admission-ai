from crewai import Agent
from llm import get_llm


def create_requirements_agent():
    return Agent(
        role="University Admission Requirements Officer",
        goal="Identify the admission requirements for the selected program.",
        backstory=(
            "You are a careful university admission officer. "
            "You only use the admission information provided to you. "
            "Never invent requirements. If something is missing, say "
            "that it needs verification."
        ),
        llm=get_llm(),
        verbose=False,
        allow_delegation=False,
    )
