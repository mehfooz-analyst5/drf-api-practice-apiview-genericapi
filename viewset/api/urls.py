"""
Student Api's
"""


from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', views.StudentsApiView, basename='students')


urlpatterns = [

    path('', include(router.urls))

]
