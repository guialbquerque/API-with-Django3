from rest_framework import viewsets, generics
from school.models import Registration, Student, Course
from school.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer, ListRegistrationStudentSerializer, ListStudentsRegisteredSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentsViewSet(viewsets.ModelViewSet):
    """Showing all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CoursesViewSet(viewsets.ModelViewSet):
    """Showing all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RegistrationsViewSet(viewsets.ModelViewSet):
    """Showing all registrations"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListRegistrationsStudent(generics.ListAPIView):
    """Listing all the registrations of the student"""
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListRegistrationStudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListStudentsRegistered(generics.ListAPIView):
    """Listing all students registred in one specific course"""
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListStudentsRegisteredSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
