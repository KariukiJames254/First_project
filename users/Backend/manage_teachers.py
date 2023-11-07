from django.forms import model_to_dict

from base.Backend.services import TeacherService, SpinSchoolUsersService
from django.db import transaction as trx
from django.contrib.auth.decorators import login_required


class ManipulateTeachers(object):

    @staticmethod
    @trx.atomic
    @login_required
    def create_teacher(**kwargs):
        sid = trx.savepoint()
        try:
            username = kwargs.get('username')
            if not username:
                return {"code": "100.000.011", 'message': 'Please provide username!'}
            first_name = kwargs.get('first_name')
            if not first_name:
                return {"code": "100.000.011", 'message': 'Please provide first_name!'}
            last_name = kwargs.get('last_name')
            if not last_name:
                return {"code": "100.000.011", 'message': 'Please provide last_name!'}
            email = kwargs.get('email')
            if not email:
                return {"code": "100.000.011", 'message': 'Please provide email!'}
            contacts = kwargs.get('mobile'
                                  '')
            if not contacts:
                return {"code": "100.000.011", 'message': 'Please provide mobile!'}
            # with transaction.atomic():
            user = SpinSchoolUsersService().filter(username=username)
            if user:
                return {"code": '100.000.011', "message": "username already exists"}
            created_user = SpinSchoolUsersService().create(
                first_name=first_name, username=username, last_name=last_name, email=email)

            if not created_user:
                return {"code": '100.000.011', "message": "Failed"}
            created_teacher = TeacherService().create(
                user=created_user, mobile=contacts)
            print("teacher created successfully")
            return {"code": "100.000.000", "message": "Success", "data": model_to_dict(created_teacher)}
        except Exception as ex:
            trx.savepoint_rollback(sid)
            print("Error during user registration", ex)
            return {"code": '100.000.011', "message": "Failed"}

    @staticmethod
    def update_teacher(**kwargs):
        try:
            teacher_id = kwargs.get('teacher_id')
            username = kwargs.get('username')
            first_name = kwargs.get('first_name')
            last_name = kwargs.get('last_name')
            email = kwargs.get('email')
            mobile = kwargs.get('mobile')

            if not teacher_id:
                return {"code": "100.000.012", 'message': 'Please provide teacher ID!'}
            teacher = TeacherService().get(id=teacher_id)
            if not teacher:
                return {"code": "100.000.012", 'message': 'teacher not found!'}
            if not username:
                username = teacher.user.username
            if not first_name:
                first_name = teacher.user.first_name
            if not last_name:
                last_name = teacher.user.last_name
            if not mobile:
                mobile = teacher.user.mobile
            if not email:
                email = teacher.user.email
            user = SpinSchoolUsersService().get(id=teacher.user.id)
            print(user.first_name)
            if user:
                SpinSchoolUsersService().update(pk=user.id, first_name=first_name, username=username,
                                                last_name=last_name, email=email, mobile=mobile)
            updated_teacher = TeacherService().update(
                pk=teacher.id, user=user)
            print("Student updated successfully")
            return {"code": "100.000.000", "message": "Success", "data": model_to_dict(updated_teacher)}
        except Exception as ex:
            print("Error during user registration", ex)
            return {"code": '100.000.012', "message": "Failed"}

    @staticmethod
    def get_single_teacher(**kwargs):
        try:
            teacher_id = kwargs.get('teacher_id')
            username = kwargs.get('username')
            email = kwargs.get('email')
            if teacher_id:
                teacher = TeacherService().get(id=teacher_id)
            elif username:
                teacher = TeacherService().get(user__username=username)
            elif email:
                teacher = TeacherService().get(email=email)
            else:
                return {"code": "100.000.013", 'message': 'teacher not found!'}

            print("teacher retrieved successfully")
            return {"code": "100.000.000", "message": "Success", "data": model_to_dict(teacher)}
        except Exception as ex:
            print("Error during retrieval", ex)
            return {"code": '100.000.013', "message": "Failed"}

    @staticmethod
    def get_teacher():
        try:
            teacher = TeacherService().filter()
            print("teacher retrieved successfully")
            return {"code": "100.000.000", "message": "Success", "data": model_to_dict(teacher)}

        except Exception as ex:
            print("Error during retrieval", ex)
        return {"code": '100.000.014', "message": "Failed"}

    @staticmethod
    def delete_teacher(**kwargs):
        try:
            teacher_id = kwargs.get('teacher_id')
            username = kwargs.get('username')
            email = kwargs.get('email')
            if teacher_id:
                teacher = TeacherService().get(id=teacher_id).delete()
            elif username:
                teacher = TeacherService().get(user__username=username).delete()
            elif email:
                teacher = TeacherService().get(email=email).delete()
            else:
                return {"code": "100.000.014", 'message': 'teacher not found!'}

            print("teacher deleted successfully")
            return {"code": "100.000.000", "message": "Success", "data": teacher}

        except Exception as ex:
            print("Error during delete", ex)
        return {"code": '100.000.014', "message": "Failed"}
