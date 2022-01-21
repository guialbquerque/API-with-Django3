from re import M
from rest_framework import serializers
from school.models import Student, Course, Registration


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'cpf', 'date_birth']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        exclude = []


class ListRegistrationStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source = 'course.description')
    time_course = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = ['course', 'time_course']
    
    def get_time_course(self, obj):
        return obj.get_time_course_display()