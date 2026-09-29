from crewai import Crew, Process, Task

from agents.requirements_agent import create_requirements_agent
from agents.eligibility_agent import create_eligibility_agent
from agents.recommendation_agent import create_recommendation_agent


def run_admission_crew(student_profile, admission_requirements):
    requirements_agent = create_requirements_agent()
    eligibility_agent = create_eligibility_agent()
    recommendation_agent = create_recommendation_agent()

    requirements_task = Task(
        description=f"""
Read the following university admission information:

{admission_requirements}

Identify the important requirements for the student's target program.

Include:
- Minimum education
- Minimum CGPA or marks
- Required subjects
- Test requirements
- English/language requirements
- Work experience requirements
- Required documents
- Other stated conditions

Do not invent anything.
If information is not provided, write "Needs verification".
""",
        expected_output=(
            "A clear list of the admission requirements for the target program."
        ),
        agent=requirements_agent,
    )

    eligibility_task = Task(
        description=f"""
Evaluate this student:

{student_profile}

Compare the student with the admission requirements identified by
the Requirements Agent.

For each major requirement, use one of:
- MET
- NOT MET
- NEEDS VERIFICATION

Explain the reason briefly.

Do not assume information that the student did not provide.
""",
        expected_output=(
            "A simple eligibility assessment showing MET, NOT MET, "
            "and NEEDS VERIFICATION items."
        ),
        agent=eligibility_agent,
        context=[requirements_task],
    )

    recommendation_task = Task(
        description=f"""
Review the student profile:

{student_profile}

Use the admission requirements and eligibility assessment from the
previous agents.

Suggest suitable programs from the university information provided.

For each suggested program, briefly explain why it may fit the student.

Do not guarantee admission.
""",
        expected_output=(
            "A concise list of potentially suitable programs with a short "
            "explanation for each."
        ),
        agent=recommendation_agent,
        context=[requirements_task, eligibility_task],
    )

    crew = Crew(
        agents=[
            requirements_agent,
            eligibility_agent,
            recommendation_agent,
        ],
        tasks=[
            requirements_task,
            eligibility_task,
            recommendation_task,
        ],
        process=Process.sequential,
        verbose=False,
    )

    return crew.kickoff()
