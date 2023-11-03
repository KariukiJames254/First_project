from django.contrib import admin

from base.models import BaseModel, GenericBaseModel, State
from school.models import Student, Grades, Subject, Teacher, Classes, JointStudentSubjectClass, StudentScore

# Register your models here.
# admin.site.register(BaseModel)
# admin.site.register(GenericBaseModel)

admin.site.register(State)


@admin.register(Student)
class StudentAdminSite(admin.ModelAdmin):
    model = Student
    list_display = ['user']
    search_fields = ['user__first_name', 'user__last_name', 'user__username', 'user__email', 'Fees', 'user__gender']
    list_filter = ['user__first_name', 'user__last_name', 'user__username', 'user__email', 'user__gender']
    ordering = ['user__first_name', 'user__last_name', 'user__username', 'user__email', 'Fees', 'user__gender']


@admin.register(Grades)
class GradeAdminSite(admin.ModelAdmin):
    list_display = ['grade', 'name', 'id', 'date_created', 'date_modified']
    search_fields = ['grade', 'name', 'id', 'date_created', 'date_modified']
    list_filter = ['date_created', 'date_modified']
    ordering = ['grade']


@admin.register(Teacher)
class TeacherAdminSite(admin.ModelAdmin):
    model = Teacher
    list_display = ['user']
    search_fields = ['user__first_name', 'user__last_name', 'user__username', 'user__email', 'user__gender']
    list_filter = ['user__first_name', 'user__last_name', 'user__username', 'user__email', 'user__gender']
    ordering = ['user__first_name', 'user__last_name', 'user__username', 'user__email', 'user__gender']


@admin.register(Subject)
class SubjectAdminSite(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']


@admin.register(Classes)
class ClassAdminSite(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    list_filter = ['name']


@admin.register(JointStudentSubjectClass)
class JoinAdminSite(admin.ModelAdmin):
    list_display = ('Student', 'Subject', 'Classes', 'state')
    search_fields = ['Student']


@admin.register(StudentScore)
class StudentScoreAdminSite(admin.ModelAdmin):
    list_display = ['students', 'form', 'score', 'subject']
    search_fields = ['subject']
    ordering = ['subject']
