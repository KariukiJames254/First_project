
from base.Backend.services import TeacherService, StudentService, JointStudentSubjectClassService, SubjectService

teachers = TeacherService().get(id="")
print(teachers)

student = StudentService().get(id="")
print(student)

subject = SubjectService().get(id="")
print(subject)

joint = JointStudentSubjectClassService().update(pk="")
print(joint)

