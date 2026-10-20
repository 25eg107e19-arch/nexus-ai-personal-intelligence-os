import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="NEXUS AI",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #080d1b, #111b32);
    color: white;
}
h1, h2, h3 {
    color: #70e1ff !important;
}
div.stButton > button {
    border-radius: 12px;
    border: 1px solid #70e1ff;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 NEXUS AI")
st.subheader("PERSONAL INTELLIGENCE OS")
st.caption("One dashboard. Your goals. Your next level.")

st.info(
    "Welcome to your personal command center. "
    "Choose a tool from the menu to get started."
)

page = st.sidebar.radio(
    "COMMAND CENTER",
    [
        "Dashboard",
        "AI Study Assistant",
        "Mission Planner",
        "Progress Tracker"
    ]
)

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if page == "Dashboard":
    st.header("🚀 Mission Control")
    st.write(f"Today's date: {date.today()}")

    c1, c2, c3 = st.columns(3)
    c1.metric("Tasks created", len(st.session_state.tasks))
    c2.metric(
        "Tasks completed",
        sum(t["done"] for t in st.session_state.tasks)
    )
    c3.metric("Modules", "3")

    st.markdown("### Your command center")
    st.write("🧠 Learn smarter")
    st.write("🎯 Plan your missions")
    st.write("📈 Track your progress")

elif page == "AI Study Assistant":
    st.header("🧠 AI Study Assistant")
    topic = st.text_input("Enter a topic to study")

    level = st.selectbox(
        "Choose your level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    if st.button("Create study guide"):
        if topic.strip():
            st.subheader(f"Study plan: {topic}")
            st.write(f"Level: {level}")
            st.write("1. Learn the basic definitions.")
            st.write("2. Understand the key concepts.")
            st.write("3. Study practical examples.")
            st.write("4. Test yourself with practice questions.")
            st.caption(
                "This starter version creates a template, "
                "not an AI-generated explanation."
            )
        else:
            st.warning("Please enter a topic first.")

elif page == "Mission Planner":
    st.header("🎯 Mission Planner")
    task = st.text_input("Your next mission")

    if st.button("Add mission"):
        if task.strip():
            st.session_state.tasks.append({
                "task": task.strip(),
                "done": False
            })
            st.rerun()
        else:
            st.warning("Enter a mission first.")

    for i, item in enumerate(st.session_state.tasks):
        st.session_state.tasks[i]["done"] = st.checkbox(
            item["task"],
            value=item["done"],
            key=f"task_{i}"
        )

elif page == "Progress Tracker":
    st.header("📈 Progress Tracker")

    total = len(st.session_state.tasks)
    completed = sum(
        item["done"] for item in st.session_state.tasks
    )

    st.metric("Completed missions", f"{completed}/{total}")
    st.progress(completed / total if total else 0)

    if total:
        chart = pd.DataFrame({
            "Status": ["Completed", "Remaining"],
            "Tasks": [completed, total - completed]
        })
        st.bar_chart(chart, x="Status", y="Tasks")

st.divider()
st.caption("NEXUS AI | Personal project built with Python + Streamlit")
