class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _avg_grade(self):
        list_of_grades = []
        for i in self.grades:
            for grade in self.grades.values():
                list_of_grades += grade
        avg_grade = "%.2f" % (sum(list_of_grades) / len(list_of_grades))
        return avg_grade

    def __str__(self):

        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._avg_grade()}\n' \
              f'Курсы в процессе обучения: {", ".join(str(i) for i in self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(str(i) for i in self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент!')
            return
        res = self._avg_grade() < other._avg_grade()
        if res:
            return f'У студента {other.name} оценки лучше, чем у студента {self.name}!'
        else:
            return f'У студента {self.name} оценки лучше, чем у студента {other.name}!'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _avg_grade(self):
        list_of_grades = []
        for i in self.grades:
            for grade in self.grades.values():
                list_of_grades += grade
        avg_grade = "%.2f" % (sum(list_of_grades) / len(list_of_grades))
        return avg_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._avg_grade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        res = self._avg_grade() < other._avg_grade()
        if res:
            return f'У лектора {other.name} оценки лучше, чем у лектора {self.name}!'
        else:
            return f'У лектора {self.name} оценки лучше, чем у лектора {other.name}!'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
# ЗАДАНИЕ НОМЕР 4


    # ТЕСТЫ


# Создание учеников
best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']
bad_student = Student('Bill', 'Gates', 'male')
bad_student.courses_in_progress += ['Java']
bad_student.finished_courses += ['Python']
avg_student = Student('Robert', 'Pale', 'male')
avg_student.courses_in_progress += ['Python']
avg_student.finished_courses += ['Java']
perfect_student = Student('Hermione', 'Granger', 'female')
perfect_student.courses_in_progress += ['Java']
perfect_student.finished_courses += ['Python']
# Создание менторов
cool_mentor = Mentor('Tom', 'Hanks')
cool_mentor.courses_attached += ['Python']
normal_mentor = Mentor('Jon', 'Snow')
normal_mentor.courses_attached += ['Java']
# Создание лекторов
new_lecturer = Lecturer('Ivan', 'Ivanov')
new_lecturer.courses_attached += ['Python']
old_lecturer = Lecturer('Daenerys', 'Targaryen')
old_lecturer.courses_attached += ['Java']
fairly_new_lecturer = Lecturer('Catherine', 'Shulman')
fairly_new_lecturer.courses_attached += ['Java']
# Создание проверяющих
awesome_reviewer = Reviewer('Tyrion', 'Lannister')
awesome_reviewer.courses_attached += ['Python']
good_reviewer = Reviewer('Steve', 'Jobs')
good_reviewer.courses_attached += ['Java']
# Выставление оценок
best_student.rate_lecturer(new_lecturer, 'Python', 10)
best_student.rate_lecturer(new_lecturer, 'Python', 9)
bad_student.rate_lecturer(old_lecturer, 'Java', 10)
bad_student.rate_lecturer(old_lecturer, 'Java', 2)
avg_student.rate_lecturer(new_lecturer, 'Python', 8)
avg_student.rate_lecturer(new_lecturer, 'Python', 9)
perfect_student.rate_lecturer(fairly_new_lecturer, 'Java', 10)
perfect_student.rate_lecturer(fairly_new_lecturer, 'Java', 10)
awesome_reviewer.rate_hw(best_student, 'Python', 10)
awesome_reviewer.rate_hw(best_student, 'Python', 9)
awesome_reviewer.rate_hw(best_student, 'Python', 10)
good_reviewer.rate_hw(bad_student, 'Java', 4)
good_reviewer.rate_hw(bad_student, 'Java', 6)
good_reviewer.rate_hw(bad_student, 'Java', 3)
awesome_reviewer.rate_hw(avg_student, 'Python', 5)
awesome_reviewer.rate_hw(avg_student, 'Python', 6)
awesome_reviewer.rate_hw(avg_student, 'Python', 6)
good_reviewer.rate_hw(perfect_student, 'Java', 10)
good_reviewer.rate_hw(perfect_student, 'Java', 10)
good_reviewer.rate_hw(perfect_student, 'Java', 10)
# Вызов методов 
print(good_reviewer)
print()
print(new_lecturer)
print()
print(best_student)
print()
print(bad_student.__lt__(best_student))
print()
print(new_lecturer.__lt__(old_lecturer))
# ЗАДАНИЕ НОМЕР 4
list_of_students = [best_student, avg_student]
list_of_lecturers = [old_lecturer, fairly_new_lecturer]


def avg_course_grade(students, course):
    all_grades = []
    for i in students:
        grades = i.grades.get(course)
        all_grades.append(sum(grades) / len(grades))
    return f'Средняя оценка по курсу {course} = '"%.2f" % (sum(all_grades) / len(students))


def avg_lectures_grade(lecturers, course):
    all_grades = []
    for i in lecturers:
        grades = i.grades.get(course)
        all_grades.append(sum(grades) / len(grades))
    return f'Средняя оценка по лекциям {course} = '"%.2f" % (sum(all_grades) / len(lecturers))


print(avg_course_grade(list_of_students, 'Python'))
print(avg_lectures_grade(list_of_lecturers, 'Java'))






