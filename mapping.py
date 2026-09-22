class Course:
    def __init__(self, title):
        self.title = title
        self.students = []

    def get_title(self):
        return self.title

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
            print(student.full_name, student.id_num,"is not enrolled in", self.title)


class Student:
    def __init__(self, id_number, full_name):
        self.id_num = id_number
        self.full_name = full_name

    def enroll_in(self, course):
        course.add_student(self)
        print(self.full_name, self.id_num, "has been added to", course.get_title())

    def drop_from(self, course):
        course.remove_student(self)
        print(self.full_name, self.id_num, "has been removed from", course.get_title())


course = Course("Computer Science 2")

student1 = Student("2026-010", "Miguel Santos")
student2 = Student("2026-223", "Mark Villar")

print(course.get_title())

student1.enroll_in(course)
student2.enroll_in(course)

print([s.full_name for s in course.students])

student1.drop_from(course)

print([s.full_name for s in course.students])
