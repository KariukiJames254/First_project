from django.forms import model_to_dict

from base.Backend.services import GradesService, JointStudentSubjectClassService, StudentscoreService, SubjectService, \
    StudentService
from school.models import Student, Grades


class AssignGrades(object):

    @staticmethod
    def generate_grades(score):
        try:
            if not score:
                return {"code": "100.000.008", "message": "Please provide score"}
            grade = None
            if score >= 70:
                grade = GradesService().get(grade='A')
            elif score >= 60 and 69 >= score:
                grade = GradesService().get(grade='B', name='Above Average')
            elif score >= 50 and score <= 59:
                grade = GradesService().get(grade='C', name='Average')
            elif score >= 40 and score <= 49:
                grade = GradesService().get(grade='D', name='pass')
            else:
                grade = GradesService().get(grade='E', name='Fail')
            return {"code": "100.000.000", "message": "success", "data": model_to_dict(grade)}
        except Exception as ex:
            print("Error during student grading", ex)
            return {"code": '100.000.008', "message": "Failed"}

    @staticmethod
    def create_grades(**kwargs):
        student_id = kwargs.get('student_id')
        subject = kwargs.get('subject')
        score = kwargs.get('score')
        student = StudentService().get(id=student_id)
        student_grade = AssignGrades().generate_grades(score)
        joint_student_table = JointStudentSubjectClassService().get(student=student)
        form = joint_student_table.Classes
        data = StudentscoreService().create(
            student=student, form=form,
            grade=GradesService().get(grade=student_grade['data']['grade']),
            subject=SubjectService().get(name=subject)
        )
        print(model_to_dict(data))

