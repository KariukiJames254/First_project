from django.contrib import admin

from base.models import BaseModel, GenericBaseModel, State
from school.models import Student, Grades, Subject, Teacher, Classes, JointStudentSubjectClass

# Register your models here.
admin.site.register(BaseModel)
admin.site.register(GenericBaseModel)
admin.site.register(Subject)
admin.site.register(Classes)
admin.site.register(State)
admin.site.register(JointStudentSubjectClass)


@admin.register(Student)
class StudentAdminSite(admin.ModelAdmin):
    model = Student
    list_display = ['first_name', 'last_name', 'username', 'email', 'Fees', 'gender']
    search_fields = ['first_name', 'last_name', 'email', 'username']
    list_filter = ['first_name', 'last_name', 'email', 'username']
    ordering = ['first_name', 'last_name', 'email', 'username']


@admin.register(Grades)
class GradeAdminSite(admin.ModelAdmin):
    list_display = ['grades', 'id', 'date_created', 'date_modified']
    search_fields = ['grades', 'id', 'date_created', 'date_modified']
    list_filter = ['date_created', 'date_modified']


@admin.register(Teacher)
class TeacherAdminSite(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'email', 'gender']
    search_fields = ['first_name', 'last_name', 'email', 'username']
    list_filter = ['first_name', 'last_name', 'email', 'username']
    ordering = ['first_name', 'last_name', 'email', 'username']
