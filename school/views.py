from rest_framework import viewsets, generics
from school.models import Registration, Student, Course
from school.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer, ListRegistrationStudentSerializer

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

class ListRegistrationsStudent(generics.ListAPIView):
    """Listing all the registrations of the student"""
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListRegistrationStudentSerializer
