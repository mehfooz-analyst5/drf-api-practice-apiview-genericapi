"""
Student Api's
"""


from django.urls import path, include
from api import views


urlpatterns = [

    path('students/', views.StudentApiView.as_view(), name='students'),

    path('students/<int:pk>/', views.StudentApiView.as_view(), name='students-detail'),


]
