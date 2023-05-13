from django.urls import path
from .views import StudentsList

urlpatterns = [
    path('students/', StudentsList.as_view(), name='students-list'),
]
