from classes.form import Form
from classes.student import Student
from classes.subject import Subject
#from classes.comboBox import create_combo
from classes.achievement import Achivment

def FillAchivement(frame):
    frame.clear_frame()

    subject_combo = Form.create_combo(Subject.getSubjects(), "Предмет", frame.obj, 1, 1)
    score = Form.create_input("Оценка", frame.obj, 2, 1)
    # math = Form.create_input("Оценка по Математике", frame.obj, 2, 1)
    # phys = Form.create_input("Оценка по Физике", frame.obj, 3, 1)
    # chem = Form.create_input("Оценка по Химии", frame.obj, 4, 1)
    btn = Form.create_button(
        frame.obj,
        'Добавить',  # Надпись на кнопке.
        lambda: Achivment.addAchivment(
            subject_combo.get(),
            1,
            int(score.get())
            # int(math.get()),
            # int(phys.get()),
            # int(chem.get()),
        ),
        5, 1, 3
    )


