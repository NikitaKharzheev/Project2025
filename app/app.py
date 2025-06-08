import streamlit as st
from student_prompt import format_student_prompt
from retriever import get_relevant_projects
from llm_wrapper import call_llm

st.set_page_config(page_title="LLM-помощник: выбор проекта", layout="wide")
st.title("🎓 Рекомендательная система научных проектов")

st.markdown("Введите информацию о себе:")

fio = st.text_input("ФИО")
email = st.text_input("Почта")
gpa = st.text_input("GPA")
interests = st.text_area("Научные интересы (фолксономия)")
about = st.text_area("Рассказ о себе")

if st.button("🔍 Подобрать проекты"):
    student_info = {
        "ФИО": fio,
        "Почта": email,
        "GPA": gpa,
        "Научные интересы (Фолксономия)": interests,
        "Рассказ о себе": about
    }

    with st.spinner("Ищем подходящие проекты..."):
        student_prompt = format_student_prompt(student_info)
        context = get_relevant_projects(student_prompt)
        recommendation = call_llm(student_prompt, context)

    st.subheader("✅ Рекомендованные проекты")
    st.markdown(recommendation)
