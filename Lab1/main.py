from datetime import datetime

from staff import PersonalInfo
from staff import Student
from staff import Professor
from course import Course
from course import CourseInfo

date = datetime.today()

student_info = PersonalInfo("Vitalii", "Lynva", "Franka Iv. 56 ", "Vitalii@lab1.com", 380974140152)
student_1 = Student(student_info, 32795, 1)
student_1.__str__()

course_info = CourseInfo("Design Patterns", datetime(2021, 10, 11), 0, 20)
course1 = Course(1, course_info)
course1.__str__()

professor_info = PersonalInfo("Jack", "Wolfskin", "Abraham Lincoln 43", "professor.wolfskin@lab1.com", 380635493379)
professor_1 = Professor(10800, professor_info)
professor_1.__str__()

print("\nEnroll student")
student_1.enroll(course1)
student_1.taken_courses()
print("\nUnroll student")
student_1.unroll(course1)
student_1.taken_courses()

print("\n")
course1.add_student(32795)
student_1.can_enroll(course1)
course1.remove_student(32795)
