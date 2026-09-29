import streamlit as st

from crew import run_admission_crew


st.set_page_config(
    page_title="University Admission AI",
    page_icon="🎓",
    layout="wide",
)

st.title("🎓 University Admission AI")
st.write(
    "A simple multi-agent university admission assistant powered by "
    "CrewAI and Groq."
)

st.info(
    "Beginner version: Requirements → Eligibility → Program Recommendation"
)

st.header("1. Student Information")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Student Name")
    degree = st.text_input(
        "Previous Degree",
        placeholder="Example: BBA",
    )
    cgpa = st.text_input(
        "CGPA / Marks",
        placeholder="Example: 3.12 / 4.00",
    )

with col2:
    subjects = st.text_area(
        "Major Subjects",
        placeholder="Finance, Accounting, Economics, Statistics",
    )
    interests = st.text_area(
        "Academic / Career Interests",
        placeholder="Finance, Banking, FinTech",
    )
    target_program = st.text_input(
        "Target Program",
        placeholder="Example: MS Finance",
    )

st.header("2. University Admission Requirements")

admission_requirements = st.text_area(
    "Paste the official admission requirements here",
    height=300,
    placeholder="""Example:

MS Finance

Minimum qualification:
16 years of education in Business, Finance,
Economics, Accounting, or a related field.

Minimum CGPA:
2.75 / 4.00

Required subjects:
Finance
Accounting
Statistics

Admission test:
University admission test

English requirement:
As specified by the university.

Required documents:
Degree certificate
Official transcript
CNIC/passport
Photographs
""",
)

student_profile = f"""
Student Name: {name}
Previous Degree: {degree}
CGPA / Marks: {cgpa}
Major Subjects: {subjects}
Academic / Career Interests: {interests}
Target Program: {target_program}
"""

st.header("3. Analyze Admission")

if st.button(
    "🚀 Start Admission Analysis",
    type="primary",
    use_container_width=True,
):
    if not name.strip():
        st.warning("Please enter the student's name.")
    elif not degree.strip():
        st.warning("Please enter the student's previous degree.")
    elif not admission_requirements.strip():
        st.warning("Please paste the university admission requirements.")
    else:
        try:
            with st.spinner("🤖 Three agents are working sequentially..."):
                result = run_admission_crew(
                    student_profile=student_profile,
                    admission_requirements=admission_requirements,
                )

            st.success("Analysis completed!")
            st.header("📋 Admission Analysis")
            st.markdown(str(result))

            st.divider()
            st.caption(
                "This is an AI-assisted preliminary assessment. "
                "The university's official admissions office makes the final "
                "admission decision."
            )

        except Exception as e:
            st.error("The application encountered an error.")
            st.code(str(e))

with st.expander("ℹ️ How this system works"):
    st.markdown(
        """
**Agent 1 — Requirements Agent**
Reads the university admission requirements.

**Agent 2 — Eligibility Agent**
Compares the student with those requirements.

**Agent 3 — Recommendation Agent**
Suggests potentially suitable programs.

The workflow is:

Requirements → Eligibility → Recommendation
"""
    )
