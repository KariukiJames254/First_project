from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from base.common.engine import get_request_data
from users.Backend.authentication_system import RegisterUser
from users.Backend.manage_students import ManipulateStudents
from users.Backend.manage_teachers import ManipulateTeachers


# Create your views here.
class SpinSchoolEndpoints(object):
    @staticmethod
    @csrf_exempt
    def create_spin_school_student(request):
        try:
            data = get_request_data(request)
            print(data)
            return JsonResponse(ManipulateStudents().create_student(**data), safe=False)
        except Exception as ex:
            print(ex)
            return {"code": "999.999.999"}

    @staticmethod
    @csrf_exempt
    def create_spin_school_teacher(request):
        try:
            data = get_request_data(request)
            return JsonResponse(ManipulateTeachers().create_teacher(**data), safe=False)
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "999.999.999"})

    @staticmethod
    @csrf_exempt
    def update_spin_school_teacher(request):
        try:
            data = get_request_data(request)
            return JsonResponse(ManipulateTeachers().update_teacher(**data), safe=False)
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "999.999.999"})

    @staticmethod
    @csrf_exempt
    def get_all_teachers(request):
        try:
            data = get_request_data(request)
            return JsonResponse(ManipulateTeachers().get_teacher(), safe=False)
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "999.999.999"})

    @staticmethod
    @csrf_exempt
    def get_single_teachers(request):
        try:
            data = get_request_data(request)
            return JsonResponse(ManipulateTeachers().get_single_teacher(**data), safe=False)
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "999.999.999"})

    @staticmethod
    @csrf_exempt
    def get_total_teachers(request):
        try:
            data = get_request_data(request)
            return JsonResponse(ManipulateTeachers().total_teachers(), safe=False)
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "999.999.999"})

    @staticmethod
    @csrf_exempt
    def update_spin_school_student(request):
        try:
            data = get_request_data(request)
            return JsonResponse(ManipulateStudents().update_student(**data), safe=False)
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "999.999.999"})

    @staticmethod
    @csrf_exempt
    def get_all_students(request):
        try:
            data = get_request_data(request)
            return JsonResponse(ManipulateStudents().get_student(), safe=False)
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "999.999.999"})

    @staticmethod
    @csrf_exempt
    def get_total_students(request):
        try:
            data = get_request_data(request)
            return JsonResponse(ManipulateStudents().total_students(), safe=False)
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "999.999.999"})




    @staticmethod
    @csrf_exempt
    def get_single_students(request):
        try:
            data = get_request_data(request)
            return JsonResponse(ManipulateStudents().get_single_student(**data), safe=False)
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "999.999.999"})

    @staticmethod
    @csrf_exempt
    def register_a_user(request):
        try:
            data = get_request_data(request)
            return JsonResponse(RegisterUser().register_user(**data), safe=False)
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "999.999.999"})

    @csrf_exempt
    def log_in_user(self, request):
        try:
            data = get_request_data(request)
            return JsonResponse(RegisterUser().login_user(request=request, **data), safe=False)
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "999.999.999"})

    @csrf_exempt
    def log_out_user(self, request):
        try:
            data = get_request_data(request)
            return JsonResponse(RegisterUser().logout_user(request=request, **data), safe=False)
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "999.999.999"})
