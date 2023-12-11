from django.db.models import Q
from django.forms import model_to_dict

from base.Backend.services import *


class Search(object):

    @staticmethod
    def search_bar(**kwargs):
        try:
            print(kwargs)
            search_name = kwargs.get('search')
            table_name = kwargs.get('table')
            list_obj = list()

            if table_name == 'user':
                object_list = SpinSchoolUsersService().filter(
                    Q(first_name=search_name)) | SpinSchoolUsersService().filter(Q(last_name=search_name))

                for x in object_list:
                    students_dict = {"id": x.id,
                                     "username": x.user.username,
                                     "first_name": x.user.first_name,
                                     "last_name": x.user.last_name,
                                     "email": x.user.email,
                                     "mobile": x.user.mobile,
                                     "gender": x.user.gender,
                                     }
                    print(students_dict)
                    list_obj.append(students_dict)

            elif table_name == 'Teacher':
                object_list = TeacherService().filter(
                    Q(user__first_name__icontains=search_name)) | TeacherService().filter(
                    Q(user__first_name__icontains=search_name))
                for x in object_list:
                    print(x)
                    teachers_dict = {"id": x.id,
                                     "username": x.user.username,
                                     "first_name": x.user.first_name,
                                     "last_name": x.user.last_name,
                                     "email": x.user.email,
                                     "mobile": x.user.mobile,
                                     "gender": x.user.gender,
                                     }
                    print(teachers_dict)
                    list_obj.append(teachers_dict)

            elif table_name == 'student':
                object_list = StudentService().filter(
                    Q(user__first_name__icontains=search_name)) | StudentService().filter(
                    Q(user__first_name__icontains=search_name))
                for x in object_list:
                    student_dict = {
                                    "username": x.user.username,
                                    "first_name": x.user.first_name,
                                    "last_name": x.user.last_name,
                                    "email": x.user.email,
                                    "mobile": x.user.mobile,
                                    "gender": x.user.gender,
                                    }
                    print(student_dict)
                    list_obj.append(student_dict)

            elif table_name == 'class':
                object_list = ClassService().filter(name=search_name)
                for x in object_list:
                    list_obj.append(x.name)

            elif table_name == 'subject':
                object_list = SubjectService().filter(name=search_name)
                for x in object_list:
                    list_obj.append(x.name)
            return {"code": "100.000.000", "message": "Success", "data": list_obj}

        except Exception as ex:
            print("Error during search", ex)
        return {"code": '100.000.044', "message": "Failed"}
