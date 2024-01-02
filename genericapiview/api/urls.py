"""
Student Api's
"""


from django.urls import path, include
from api import views


urlpatterns = [

    path('students/', views.StudentsApiView.as_view(), name='students'),

    path('students/<int:pk>/', views.StudentDataView.as_view(), name='students-detail'),


]
