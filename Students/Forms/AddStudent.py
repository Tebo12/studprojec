#from Students.classes.form import Form
#from Students.classes.student import Student
from classes.form import Form
from classes.student import Student


def FormAddStudent(frame):
    frame.clear_frame()

    Name = Form.create_input("Имя студента", frame.obj, 1, 1)
    #math = Form.create_input("Оценка по Математике", frame.obj, 2, 1)
    #phys = Form.create_input("Оценка по Физике", frame.obj, 3, 1)
    #chem = Form.create_input("Оценка по Химии", frame.obj, 4, 1)

    btn = Form.create_button(
        frame.obj,
        'Добавить',  # Надпись на кнопке.
        lambda: Student.add_student(
            Name.get(),
            #int(math.get()),
            #int(phys.get()),
            #int(chem.get()),
        ),
        5, 1, 3

    )