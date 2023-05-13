# from django.test import TestCase
# from .models import Student
# from django.urls import reverse
# from django.test import TestCase, Client
# from rest_framework import status
# from .models import Student
# from .serializers import StudentSerializer
# from .apps import StudentsConfig
# from .views import StudentsList

# #models.py

# class StudentModelTestCase(TestCase):
#     def setUp(self):
#         self.student = Student.objects.create(name='John')
        
#     def test_student_str_method(self):
#         self.assertEqual(str(self.student), 'John')
        
#     def test_student_name_field_max_length(self):
#         max_length = self.student._meta.get_field('name').max_length
#         self.assertEqual(max_length, 200)
        
#     def test_student_name_field_is_unique(self):
#         name_field = self.student._meta.get_field('name')
#         self.assertTrue(name_field.unique)

# #apps.py

# class StudentsConfigTestCase(TestCase):
#     def test_students_config_name(self):
#         self.assertEqual(StudentsConfig.name, 'students')
        
#     def test_students_config_auto_field(self):
#         self.assertEqual(StudentsConfig.default_auto_field, 'django.db.models.BigAutoField')


# #views.py

# class StudentsListTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.url = reverse('students-list')
#         self.student1 = Student.objects.create(name='John')
#         self.student2 = Student.objects.create(name='Alice')
        
#     def test_students_list_view_get(self):
#         response = self.client.get(self.url)
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializer.data)