from rest_framework import viewsets
from school.models import Registration, Student, Course
from school.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    """Showing all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    """Showing all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RegistrationsViewSet(viewsets.ModelViewSet):
    """Showing all registrations"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

