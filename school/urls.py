from django.urls import path

from school.views import SchoolEndpoints

urlpatterns = [
    path('search_bar/', SchoolEndpoints().search_user, name='search_bar')

]
