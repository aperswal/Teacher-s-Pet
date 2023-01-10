class Student:
  def __init__(self, class_number, name, homework_grades, test_grades):
    self.class_number = class_number
    self.name = name
    self.homework_grades = homework_grades
    self.test_grades = test_grades

students = []

def add_student(class_number, name, homework_grades, test_grades):
    student = Student(class_number, name, homework_grades, test_grades)
    students.append(student)

def print_grades():
  class_numbers = set([student.class_number for student in students])
  for class_number in class_numbers:
    print(f"Class number: {class_number}")
    for student in students:
      if student.class_number == class_number:
        print(f"    Name: {student.name} \t Homework Grades: {student.homework_grades} \t Test Grades: {student.test_grades}")
        
def print_grades_by_class_num(class_number):
    for student in students:
        if student.class_number == class_number:
            print(f"Name: {student.name} \t Homework Grades: {student.homework_grades} \t Test Grades: {student.test_grades}")
            
def print_grades_by_student(name):
    for student in students:
        if student.name == name:
            print(f"Class Number: {student.class_number} \nName: {student.name} \t Homework Grades: {student.homework_grades} \t Test Grades: {student.test_grades}")

            
                                                          
