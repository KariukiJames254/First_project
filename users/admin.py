from django.contrib import admin
from .models import SpinSchoolUsers


# Register your models here.
@admin.register(SpinSchoolUsers)
class SpinSchoolUsersAdminSite(admin.ModelAdmin):
    model = SpinSchoolUsers
    list_display = ['first_name', 'last_name', 'username', 'email', 'gender', 'id']
    search_fields = ['first_name', 'last_name', 'username', 'email', 'gender']
    list_filter = ['first_name', 'last_name', 'username', 'email', 'gender']
    ordering = ['first_name', 'last_name', 'username', 'email', 'gender']
