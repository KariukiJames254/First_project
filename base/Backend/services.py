from base.Backend.service_base import ServiceBase

from school.models import Teacher, Student, Subject, Classes, JointStudentSubjectClass, Grades, StudentScore
from users.models import SpinSchoolUsers


class TeacherService(ServiceBase):
    manager = Teacher.objects


class StudentService(ServiceBase):
    manager = Student.objects


class ClassService(ServiceBase):
    manager = Classes.objects


class GradesService(ServiceBase):
    manager = Grades.objects


class SubjectService(ServiceBase):
    manager = Subject.objects


class JointStudentSubjectClassService(ServiceBase):
    manager = JointStudentSubjectClass.objects


class SpinSchoolUsersService(ServiceBase):
    manager = SpinSchoolUsers.objects


class StudentscoreService(ServiceBase):
    manager = StudentScore.objects
