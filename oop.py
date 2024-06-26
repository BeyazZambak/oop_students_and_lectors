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
            print('Error')

    def _average_grade(self):
        grade = [grade for grades in self.grades.values() for grade in grades]
        res = round((sum(grade)/len(grade)), 1)
        return res

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_grade()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"
        return res 

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Error") 
            return
        return  self._average_grade() < other._average_grade()
        

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        grade = [grade for grades in self.grades.values() for grade in grades]
        res = round((sum(grade)/len(grade)), 1)
        return res

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade()}"
        return res  
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Error") 
            return
        return  self._average_grade() < other._average_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Error')
    
    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res

def students_average_grade(student_list, course):
    grade_list = [grade for student in student_list for grade in student.grades.get(course)]
    return sum(grade_list) / len(grade_list)

def lecturer_average_grade(lecturer_list, course):
    grade_list = [grade for lecturer in lecturer_list for grade in lecturer.grades.get(course)]
    return sum(grade_list) / len(grade_list)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

second_student = Student('Endy', 'Mitchel', 'm')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['C++']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

second_reviewer = Reviewer('Second', 'Buddy')
second_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['C++']

cool_lecturer = Lecturer("Best", "Lecturer")
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

second_lecturer = Lecturer("Second", "Lecturer")
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['C++']

best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 5)
best_student.rate_lecturer(cool_lecturer, 'Python', 8)

second_student.rate_lecturer(second_lecturer, 'Python', 9)
second_student.rate_lecturer(second_lecturer, 'Python', 5)
second_student.rate_lecturer(second_lecturer, 'Python', 8)

best_student.rate_lecturer(cool_lecturer, 'Git', 7)
best_student.rate_lecturer(cool_lecturer, 'Git', 6)
best_student.rate_lecturer(cool_lecturer, 'Git', 5)

second_student.rate_lecturer(second_lecturer, 'C++', 1)
second_student.rate_lecturer(second_lecturer, 'C++', 3)
second_student.rate_lecturer(second_lecturer, 'C++', 6)
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(second_student, 'Python', 4)
cool_reviewer.rate_hw(second_student, 'Python', 5)
cool_reviewer.rate_hw(second_student, 'Python', 9)
 
print(f"Student grades ({best_student.name} {best_student.surname}): {best_student.grades}")
print(f"Lecturer's grades ({cool_lecturer.name} {cool_lecturer.surname}): {cool_lecturer.grades}")
print()
print(cool_reviewer)
print()
print(cool_lecturer)
print()
print(best_student)
print()
print(best_student > second_student)
print()
print(best_student < second_student)
print()
print(cool_lecturer > second_lecturer)
print()
print(cool_lecturer < second_lecturer)
print()
print(students_average_grade([best_student, second_student], 'Python'))
print()
print(lecturer_average_grade([cool_lecturer, second_lecturer], 'Python'))