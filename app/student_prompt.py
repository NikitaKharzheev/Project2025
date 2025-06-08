def format_student_prompt(student):
    return (
        f"ФИО: {student['ФИО']}\n"
        f"Научные интересы: {student['Научные интересы (Фолксономия)']}\n"
        f"Рассказ о себе: {student['Рассказ о себе']}\n"
        f"GPA: {student['GPA']}\n"
    )
