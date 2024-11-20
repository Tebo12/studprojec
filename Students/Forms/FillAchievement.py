from classes.form import Form
from classes.student import Students
from classes.subject import Subjects
#from classes.comboBox import create_combo
from classes.achievement import Achievements

def FillAchivement(frame):
    frame.clear_frame()
    student_combo = Form.create_combo(Students.getStudents(), "Студент", frame.obj, 1, 1)
    subject_combo = Form.create_combo(Subjects.getSubjects(), "Предмет", frame.obj, 2, 1)
    score = Form.create_input("Оценка", frame.obj, 3, 1)
    # math = Form.create_input("Оценка по Математике", frame.obj, 2, 1)
    # phys = Form.create_input("Оценка по Физике", frame.obj, 3, 1)
    # chem = Form.create_input("Оценка по Химии", frame.obj, 4, 1)
    btn = Form.create_button(
        frame.obj,
        'Добавить',  # Надпись на кнопке.
        lambda: Achievements.addAchivment(
            {"subject_id":subject_combo.get().id,
            "student_id":student_combo.get().id,
            "score": int(score.get())}
            # int(math.get()),
            # int(phys.get()),
            # int(chem.get()),
        ),
        4, 1, 3
    )


