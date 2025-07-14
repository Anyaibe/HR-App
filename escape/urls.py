
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.dashboard, name='dashboard'),  # Set dashboard as the default page
    path("employee_directory/", views.employee_directory, name="employee_directory"),
    path("leave_directory/", views.leave_directory, name="leave_directory"),
]
