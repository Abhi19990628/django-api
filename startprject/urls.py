
from django.contrib import admin
from django.urls import path
from startapp.views import employessListView,UserListView,EmployessDetailsview

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/employe', employessListView),
    path('api/employe/<int:pk>', EmployessDetailsview),
    path('api/users', UserListView),
]
