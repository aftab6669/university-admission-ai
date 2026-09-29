from crewai import Agent
from llm import get_llm


def create_eligibility_agent():
    return Agent(
        role="Student Eligibility Officer",
        goal="Compare the student's profile with the admission requirements.",
        backstory=(
            "You are a university eligibility officer. "
            "Carefully compare the student's information with the stated "
            "requirements. Mark each important requirement as MET, NOT MET, "
            "or NEEDS VERIFICATION. Never assume missing information."
        ),
        llm=get_llm(),
        verbose=False,
        allow_delegation=False,
    )
