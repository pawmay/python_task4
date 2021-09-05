import sys

ALLOWED_USERS_TYPES = ('uczen', 'nauczyciel', 'wychowawca', 'koniec')
# ALLOWED_USERS_TYPES = ('student', 'teacher', 'tutor', 'end')

classes = {'1a': {'tutor': 'Krzysztof Baczynski', 'teachers': [{'teacher': {'name': 'Jan Dlugosz', 'course': 'Jezyk Polski'}}, {'teacher': {'name': 'Henryk Sienkiewicz', 'course': 'Historia'}}], 'students': ['Jan Brzechwa', 'Jan Dlugosz', 'Eliza Orzeszkowa']}, '1b': {'tutor': 'Krzysztof Baczynski', 'teachers': [{'teacher': {'name': 'Jan Dlugosz', 'course': 'Jezyk Polski'}}, {'teacher': {'name': 'Henryk Sienkiewicz', 'course': 'Historia'}}], 'students': ['Aleksander Fredro', 'Witold Gombrowicz']}, '2a': {'tutor': 'Krzysztof Baczynski', 'teachers': [{'teacher': {'name': 'Maria Konopnicka', 'course': 'Jezyk Polski'}}, {'teacher': {'name': 'Stanislaw Lem', 'course': 'Fizyka'}}, {'teacher': {'name': 'Henryk Sienkiewicz', 'course': 'Historia'}}], 'students': ['Hanna Krall', 'Zygmunt Krasinski', 'Jan Andrzej Morsztyn']}, '1c': {'tutor': 'Jan Brzechwa', 'teachers': [{'teacher': {'name': 'Jan Dlugosz', 'course': 'Jezyk Polski'}}], 'students': ['Zbigniew Herbert']}, '2b': {'tutor': 'Jan Brzechwa', 'teachers': [{'teacher': {'name': 'Maria Konopnicka', 'course': 'Jezyk Polski'}}, {'teacher': {'name': 'Stanislaw Lem', 'course': 'Fizyka'}}, {'teacher': {'name': 'Henryk Sienkiewicz', 'course': 'Historia'}}], 'students': ['Malgorzata Musierowicz', 'Cyprian Kamil Norwid']}, '2c': {'teachers': [{'teacher': {'name': 'Maria Konopnicka', 'course': 'Jezyk Polski'}}, {'teacher': {'name': 'Stanislaw Lem', 'course': 'Fizyka'}}], 'students': ['Boleslaw Prus', 'Juliusz Slowacki', 'Julian Tuwim', 'Stanislaw Wyspianski']}, '2d': {'teachers': [{'teacher': {'name': 'Stanislaw Lem', 'course': 'Fizyka'}}]}, '1d': {'teachers': [{'teacher': {'name': 'Henryk Sienkiewicz', 'course': 'Historia'}}]}}

phrase = sys.argv[1]

while True:
    user_type = input("Enter user type: ")

    if user_type not in ALLOWED_USERS_TYPES:
        print(f"The user type: {user_type} is not allowed. Available types of users: {ALLOWED_USERS_TYPES}")

    if user_type == 'uczen':
        student_name = input("Enter student name: ")
        class_name = input("Enter class name: ")
        if not classes.get(class_name):
            classes[class_name] = {'students': [student_name]}
        elif 'students' not in classes.get(class_name).keys():
            classes[class_name].update(students=[student_name])
        else:
            classes.get(class_name)['students'].append(student_name)
        continue
    elif user_type == 'nauczyciel':
        teacher_name = input("Enter teacher name: ")
        course_name = input("Enter course name: ")
        while True:
            class_name = input("Enter class name: ")
            if len(class_name) == 0:
                break
            if not classes.get(class_name):
                classes[class_name] = {'teachers': [{'teacher': {'name': teacher_name, 'course': course_name}}]}
            else:
                if 'teachers' in classes.get(class_name).keys():
                    teacher = {'teacher': {'name': teacher_name, 'course': course_name}}.copy()
                    classes.get(class_name)['teachers'].append(teacher)
                else:
                    classes[class_name].update(teachers=[{'teacher': {'name': teacher_name, 'course': course_name}}])
            continue
        continue
    elif user_type == 'wychowawca':
        tutor_name = input("Enter tutor name: ")
        while True:
            class_name = input("Enter class name: ")
            if len(class_name) == 0:
                break
            if not classes.get(class_name):
                classes[class_name] = {'tutor': tutor_name}
            else:
                classes[class_name].update(tutor=tutor_name)
            continue
        continue
    elif user_type == 'koniec':
        break

# phrase : class name
if classes.get(phrase):
    if 'tutor' in classes.get(phrase).keys():
        print(classes.get(phrase)['tutor'])
    if 'students' in classes.get(phrase).keys():
        for students in classes.get(phrase)['students']:
            print(students)

# phrase : tutor name
for key in classes:
    if 'tutor' in classes.get(key).keys() and 'students' in classes.get(key).keys():
        if phrase == classes.get(key)['tutor']:
            for students in classes.get(key)['students']:
                print(students)

# phrase : teacher
for key in classes:
    if 'tutor' in classes.get(key).keys() and 'teachers' in classes.get(key).keys():
        for teachers in classes.get(key)['teachers']:
            if phrase == teachers.get('teacher')['name']:
                print(classes.get(key)['tutor'])

# phrase : student
for key in classes:
    if 'students' in classes.get(key).keys() and 'teachers' in classes.get(key).keys():
        for students in classes.get(key)['students']:
            if phrase == students:
                for teachers in classes.get(key)['teachers']:
                    print(teachers.get('teacher')['course'])
                    print(teachers.get('teacher')['name'])
