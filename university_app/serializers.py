from rest_framework import serializers

from university_app.models import Student, Groupe, Teacher, Module, Session


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class GroupeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groupe
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
