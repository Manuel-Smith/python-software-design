from course import Course
from student import Student
from aifc import Error
from datetime import datetime


class Enrol:
    def __init__(self, student, course):
        if not isinstance(student, Student):
            raise Error("Invalid student....")

        if not isinstance(course, Course):
            raise Error("invalid course...")

        self.student = student
        self.course = course
        self.grade = None
        self.date = datetime.now()

    def set_grade(self, grade):
        self.grade = grade
