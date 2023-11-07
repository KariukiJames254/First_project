from django.forms import model_to_dict

from base.Backend.services import StudentService, TeacherService, ClassService, JointStudentSubjectClassService, \
    SubjectService


class StudentProfile(object):
    @staticmethod
    def create_profile(**kwargs):
        try:
            class_id = kwargs.get('class_id')
            student_id = kwargs.get('student_id')
            subject = kwargs.get('subject')
            teacher_id = kwargs.get('teacher_id')
            if not teacher_id:
                return {"code": '100.000.015', "message": "Please provide teacher_id"}
            if not subject:
                return {"code": '100.000.015', "message": "subject not found!"}
            if not student_id:
                return {"code": '100.000.015', "message": "Student id not found"}

            student = StudentService().get(id=student_id)
            teacher = TeacherService().get(id=teacher_id)
            form = ClassService().get(id=class_id)
            check = JointStudentSubjectClassService().filter(
                Student=student, Classes=form, Teacher=teacher,
                Subject=SubjectService().get(name=subject)).first()
            if check:
                return {"code": '100.000.015', "message": "Student information already exists!"}
            data = JointStudentSubjectClassService().create(
                Student=student, Classes=form,
                Teacher=teacher,
                Subject=SubjectService().get(name=subject)
            )
            return {"code": "100.000.000", "message": "Success", "data": model_to_dict(data)}

        except Exception as ex:
            print("Error during creating grades", ex)
        return {"code": '100.000.015', "message": "Failed"}
