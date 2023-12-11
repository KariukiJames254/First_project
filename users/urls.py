from django.urls import path
from users.views import SpinSchoolEndpoints

urlpatterns = [
    path('create_student/', SpinSchoolEndpoints().create_spin_school_student, name="create_student"),
    path('update_student/', SpinSchoolEndpoints().update_spin_school_student, name="update_student"),
    path('create_teacher/', SpinSchoolEndpoints().create_spin_school_teacher, name="create_teacher"),
    path('update_teacher/', SpinSchoolEndpoints().update_spin_school_teacher, name="update_teacher"),
    path('login_user/', SpinSchoolEndpoints().log_in_user, name='login_user'),
    path('logout_user/', SpinSchoolEndpoints().log_out_user, name='logout_user'),
    path('register_user/', SpinSchoolEndpoints().register_a_user, name='register_user'),
    path('get_teacher/', SpinSchoolEndpoints().get_all_teachers, name='get_teacher'),
    path('get_single_teacher/', SpinSchoolEndpoints().get_single_teachers, name='get_single_teacher'),
    path('get_student/', SpinSchoolEndpoints().get_all_students, name='get_student'),
    path('get_single_student/', SpinSchoolEndpoints().get_single_students, name='get_single_student'),
    path('total_students/', SpinSchoolEndpoints().get_total_students, name='total_students'),
    path('total_teachers/', SpinSchoolEndpoints().get_total_teachers, name='total_teachers')

]
