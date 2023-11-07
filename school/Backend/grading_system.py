from django.forms import model_to_dict

from base.Backend.services import GradesService, StudentscoreService, SubjectService, StudentService, ClassService

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
        try:
            class_id = kwargs.get('class_id')
            student_id = kwargs.get('student_id')
            subject = kwargs.get('subject')
            score = kwargs.get('score')
            if not score:
                return {"code": '100.000.008', "message": "Please provide score"}
            if not subject:
                return {"code": '100.000.008', "message": "subject not found!"}
            if not student_id:
                return {"code": '100.000.008', "message": "Student id not found"}

            student = StudentService().get(id=student_id)
            student_grade = AssignGrades().generate_grades(score)
            grade = student_grade['data']['grade']
            if not grade:
                return {"code": '100.000.008', "message": "grade not found"}

            form = ClassService().get(id=class_id)
            data = StudentscoreService().create(
                students=student, form=form,
                student_grade=GradesService().get(grade=grade),
                subject=SubjectService().get(name=subject), score=score
            )
            return {"code": "100.000.000", "message": "Success", "data": model_to_dict(data)}

        except Exception as ex:
            print("Error during creating grades", ex)
        return {"code": '100.000.008', "message": "Failed"}
