from decimal import Decimal

from django.forms import model_to_dict

from base.Backend.services import StudentService, TeacherService, SpinSchoolUsersService


class ManipulateStudents(object):
    @staticmethod
    def create_student(**kwargs):
        try:
            username = kwargs.get("username")
            print(username)
            if not username:
                return {"code": "100.000.003", 'message': 'Please provide username!'}
            first_name = kwargs.get('first_name')
            print(first_name)
            if not first_name:
                return {"code": "100.000.003", 'message': 'Please provide First_Name!'}
            last_name = kwargs.get('last_name')
            print(last_name)
            if not last_name:
                return {"code": "100.000.003", 'message': 'Please provide last_Name!'}
            contacts = kwargs.get("contacts")
            print(contacts)
            fees = kwargs.get("fees")
            print(fees)
            if not fees:
                return {"code": "100.000.003", 'message': 'Please provide last_Name!'}
            student = StudentService().filter(username=username).first()
            if student:
                print("Student already Exists", str(student.id))
                return {"code": "100.000.003", 'message': 'Student already Exists'}
            print('trying to create student.....')
            student = StudentService().create(
                Fees=Decimal(fees), first_name=first_name, last_name=last_name,
                mobile=int(contacts), username=username,
            )
            print("user created successfully")
            """
            After student is created, create their enrolment and assign them a student id
            """
            return {"code": "100.000.000", "message": "Success", "data": model_to_dict(student)}
        except Exception as ex:
            print("Error during user registration", ex)
            return {"code": '100.000.003', "message": "Failed"}

    @staticmethod
    def update_student(**kwargs):
        try:
            student_id = kwargs.get('student_id')
            username = kwargs.get('username')
            first_name = kwargs.get('first_name')
            last_name = kwargs.get('last_name')
            arrears = kwargs.get("arrears")

            fees = kwargs.get('fees')
            if not student_id:
                return {"code": "100.000.005", 'message': 'Please provide student ID!'}
            student = StudentService().get(id=student_id)
            if not student:
                return {"code": "100.000.005", 'message': 'Student not found!'}
            if not username:
                username = student.user.username
            if not first_name:
                first_name = student.user.first_name
            if not last_name:
                last_name = student.user.last_name
            if not fees:
                fees = student.fees
            if not arrears:
                arrears = student.Arrears
            user = SpinSchoolUsersService().get(id=student.user.id)
            print(user.first_name)
            if user:
                SpinSchoolUsersService().update(pk=user.id, first_name=first_name, username=username,
                                                last_name=last_name)
            updated_student = StudentService().update(
                pk=student.id, user=user, Fees=fees, Arrears=arrears)
            print("Student updated successfully")
            return {"code": "100.000.000", "message": "Success", "data": model_to_dict(updated_student)}
        except Exception as ex:
            print("Error during user registration", ex)
            return {"code": '100.000.005', "message": "Failed"}

    @staticmethod
    def get_single_student(**kwargs):
        try:
            user_id = kwargs.get('user_id')
            username = kwargs.get('username')
            email = kwargs.get('email')
            if user_id:
                student = StudentService().get(id=user_id)
            elif username:
                student = StudentService().get(user__username=username)
            elif email:
                student = StudentService().get(email=email)
            else:
                return {"code": "100.000.004", 'message': 'Student not found!'}

            print("Student retrieved successfully")
            return {"code": "100.000.000", "message": "Success", "data": model_to_dict(student)}
        except Exception as ex:
            print("Error during retrieval", ex)
            return {"code": '100.000.004', "message": "Failed"}

    @staticmethod
    def get_student():
        try:
            student = StudentService().filter()
            print("Student retrieved successfully")
            return {"code": "100.000.000", "message": "Success", "data": model_to_dict(student)}

        except Exception as ex:
            print("Error during retrieval", ex)
        return {"code": '100.000.006', "message": "Failed"}


class ModifyTeacher(object):

    @staticmethod
    def create_teacher(**kwargs):
        try:
            username = kwargs.get("username")
            print(username)
            if not username:
                return {"code": "100.000.010", 'message': 'Please provide username!'}
            first_name = kwargs.get('first_name')
            print(first_name)
            if not first_name:
                return {"code": "100.000.010", 'message': 'Please provide First_Name!'}
            last_name = kwargs.get('last_name')
            print(last_name)
            if not last_name:
                return {"code": "100.000.010", 'message': 'Please provide last_Name!'}
            contacts = kwargs.get("contacts")
            print(contacts)

            teacher = TeacherService().filter(username=username).first()
            if teacher:
                print("Student already Exists", str(teacher.id))
                return {"code": "100.000.010", 'message': 'Student already Exists'}
            print('trying to create student.....')
            teacher = TeacherService().create(
                first_name=first_name, last_name=last_name,
                mobile=int(contacts), username=username,
            )
            print("user created successfully")
            """
            After student is created, create their enrolment and assign them a student id
            """
            return {"code": "100.000.000", "message": "Success", "data": model_to_dict(teacher)}
        except Exception as ex:
            print("Error during user registration", ex)
            return {"code": '100.000.010', "message": "Failed"}

    @staticmethod
    def update_teacher(**kwargs):
        try:
            user_id = kwargs.get('user_id')
            username = kwargs.get('username')
            first_name = kwargs.get('first_name')
            last_name = kwargs.get('last_name')
            if not user_id:
                return {"code": "100.000.011", 'message': 'Please provide user ID!'}
            teacher = TeacherService().get(id=user_id)
            if not teacher:
                return {"code": "100.000.011", 'message': 'Teacher not found!'}

            teacher = TeacherService().get(id=user_id)
            updated_teacher = TeacherService().update(
                pk=teacher.id, username=username, first_name=first_name,
                last_name=last_name, )
            print("Teacher updated successfully")
            return {"code": "100.000.000", "message": "Success", "data": model_to_dict(updated_teacher)}
        except Exception as ex:
            print("Error during user registration", ex)
            return {"code": '100.000.011', "message": "Failed"}
