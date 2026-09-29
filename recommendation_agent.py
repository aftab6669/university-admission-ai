from crewai import Agent
from llm import get_llm


def create_recommendation_agent():
    return Agent(
        role="University Program Advisor",
        goal="Suggest programs that fit the student's academic background and interests.",
        backstory=(
            "You are an academic program advisor. "
            "Use the student's education, subjects, interests, and eligibility "
            "information to suggest suitable programs. "
            "Do not guarantee admission."
        ),
        llm=get_llm(),
        verbose=False,
        allow_delegation=False,
    )
