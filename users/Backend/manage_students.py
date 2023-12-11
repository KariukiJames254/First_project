from decimal import Decimal

from django.contrib.auth.hashers import make_password
from django.forms import model_to_dict
from school.Backend.registration_generator import *
from base.Backend.services import StudentService, SpinSchoolUsersService
from django.db import transaction as trx


class ManipulateStudents(object):
    @staticmethod
    @trx.atomic
    def create_student(**kwargs):
        sid = trx.savepoint()
        try:
            username = kwargs.get("username")
            if not username:
                return {"code": "100.000.003", 'message': 'Please provide username!'}
            first_name = kwargs.get('first_name')
            if not first_name:
                return {"code": "100.000.003", 'message': 'Please provide First_Name!'}
            last_name = kwargs.get('last_name')
            if not last_name:
                return {"code": "100.000.003", 'message': 'Please provide last_Name!'}
            contacts = kwargs.get("mobile")
            if not contacts:
                return {"code": "100.000.003", 'message': 'Please provide mobile!'}
            email = kwargs.get('email')
            if not email:
                return {"code": "100.000.003", 'message': 'Please provide email!'}
            password = kwargs.get('password')
            if not password:
                return {"code": "100.000.011", 'message': 'Please provide password!'}
            gender = kwargs.get('gender')

            user = SpinSchoolUsersService().filter(username=username)
            if user:
                return {"code": '100.000.003', "message": "username already exists"}
            created_user = SpinSchoolUsersService().create(
                first_name=first_name, username=username,
                last_name=last_name, mobile=contacts, email=email, gender=gender, password=make_password(password))
            if not created_user:
                return {"code": '100.000.011', "message": "Failed"}
            first_name = created_user.first_name
            last_name = created_user.last_name
            date_created = created_user.date_joined
            count = created_user.id
            count = str(count).zfill(4)
            k = {
                "first_name": first_name,
                "last_name": last_name,
                "count": count,
                'date_created': str(date_created)
            }
            student_regNo = generate_registration_number(**k)
            created_student = StudentService().create(
                Fees=Decimal(0), user=created_user, Arrears=Decimal(200000), registration_number=student_regNo
            )
            print("user created successfully")
            return {"code": "100.000.000", "message": "Success", "data": model_to_dict(created_student)}
        except Exception as ex:
            trx.savepoint_rollback(sid)
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
            gender = kwargs.get('gender')
            email = kwargs.get('email')
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
                fees = student.Fees
            if not arrears:
                arrears = student.Arrears
            if not gender:
                gender = student.gender
            if not email:
                email = student.email
            print(first_name)
            user = SpinSchoolUsersService().get(id=student.user.id)
            if user:
                SpinSchoolUsersService().update(pk=user.id, first_name=first_name, username=username,
                                                last_name=last_name, gender=gender, email=email)
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
            student_id = kwargs.get('student_id')
            student = StudentService().get(id=student_id)
            if student:
                student = {
                    "first_name": student.user.first_name,
                    "last_name": student.user.last_name,
                    "username": student.user.username,
                    "email": student.user.email,
                    "mobile": student.user.mobile,
                    "fees": student.Fees,
                    "Arrears": student.Arrears,
                    "registration_number": student.registration_number
                }
                return {"code": "100.000.000", "message": "Success", "data": student}

        except Exception as ex:
            print("Error during retrieval", ex)
            return {"code": '100.000.004', "message": str(ex)}

    @staticmethod
    def get_student():
        try:
            student_list = list()
            student = StudentService().filter()
            for x in student:
                students_dict = {"id": x.id,
                                 "username": x.user.username,
                                 "first_name": x.user.first_name,
                                 "last_name": x.user.last_name,
                                 "email": x.user.email,
                                 "mobile": x.user.mobile,
                                 "gender": x.user.gender,
                                 "Arrears": x.Arrears,
                                 "Fees": x.Fees,
                                 "registration_number": x.registration_number
                                 }
                print(students_dict)
                student_list.append(students_dict)
            print("Student retrieved successfully")
            return {"code": "100.000.000", "message": "Success", "data": student_list}
        except Exception as ex:
            print("Error during retrieval", ex)
        return {"code": '100.000.006', "message": "Failed"}

    @staticmethod
    def delete_student(**kwargs):
        try:
            student_id = kwargs.get('student_id')
            username = kwargs.get('username')
            email = kwargs.get('email')
            if student_id:
                student = StudentService().get(id=student_id).delete()
            elif username:
                student = StudentService().get(user__username=username).delete()
            elif email:
                student = StudentService().get(email=email).delete()
            else:
                return {"code": "100.000.016", 'message': 'student not found!'}

            print("student deleted successfully")
            return {"code": "100.000.000", "message": "Success", "data": student}

        except Exception as ex:
            print("Error during delete", ex)
        return {"code": '100.000.016', "message": "Failed"}

    @staticmethod
    def total_students():
        total_students_count = StudentService().filter().count()
        context = {'total_users_count': total_students_count}
        return context
