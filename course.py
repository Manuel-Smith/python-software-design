from professor import Professor
from enrol import Enrol
from aifc import Error


class Course:
    def __init__(self, name, code, min_students, max_, min_, start, professor):
        self.name = name
        self.code = code
        self.max = max_
        self.min = min_
        self.professors = []
        self.enrolments = []

        if isinstance(professor, Professor):
            self.professors.append(professor)

        elif isinstance(professor, list):
            for entry in professor:
                if not isinstance(entry, Professor):
                    raise Error("Invalid Address... ")

            self.professors = professor

        else:
            raise Error("Invalid Address...")

        def add_professor(self, professor):
            if not isinstance(professor, Professor):
                raise Error("Invalid professor...")

            self.professors.append(professor)

        def add_enrollment(self, enroll):
            if not isinstance(enroll, Enrol):
                raise Error("Invalid Enrol")

            if len(self.enrolments) == self.max:
                raise Error("Cannot enrol, course is full...")

            self.enrolments.append(enroll)

        def is_cancelled(self):
            return len(self.enrolments) < self.min
