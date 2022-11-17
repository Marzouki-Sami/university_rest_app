from io import BytesIO

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student, Groupe, Module, Teacher, Session
from .serializers import StudentSerializer, GroupeSerializer, ModuleSerializer, SessionSerializer, TeacherSerializer
from rest_framework import viewsets


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    @csrf_exempt
    def add_student(request):
        if request.method == 'POST':
            json_data = request.body
            stream = BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            serializer = StudentSerializer(data=pythondata)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Data Created'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')

    @csrf_exempt
    def student_detail(request, pk):
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return HttpResponse('{"message": "Student not found"}', status=404)
        if request.method == 'GET':
            serializer = StudentSerializer(student)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        return HttpResponse('{"message": "Bad request"}', status=400)

    @csrf_exempt
    def update_student(request, pk):
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return HttpResponse('{"message": "Student not found"}', status=404)
        if request.method == 'PUT':
            json_data = request.body
            stream = BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            serializer = StudentSerializer(student, data=pythondata)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Data Updated'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')
        return HttpResponse('{"message": "Bad request"}', status=400)

    @csrf_exempt
    def delete_student(request, pk):
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return HttpResponse('{"message": "Student not found"}', status=404)
        if request.method == 'DELETE':
            student.delete()
            res = {'msg': 'Data Deleted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        return HttpResponse('{"message": "Bad request"}', status=400)


class GroupeViewSet(viewsets.ModelViewSet):
    queryset = Groupe.objects.all()
    serializer_class = GroupeSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    @csrf_exempt
    def add_group(request):
        if request.method == 'POST':
            json_data = request.body
            stream = BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            serializer = GroupeSerializer(data=pythondata)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Data Created'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    @csrf_exempt
    def add_module(request):
        if request.method == 'POST':
            json_data = request.body
            stream = BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            serializer = ModuleSerializer(data=python_data)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Module Data Created'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    @csrf_exempt
    def add_session(request):
        if request.method == 'POST':
            json_data = request.body
            stream = BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            serializer = SessionSerializer(data=python_data)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Session Data Created'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    @csrf_exempt
    def add_teacher(request):
        if request.method == 'POST':
            json_data = request.body
            stream = BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            serializer = TeacherSerializer(data=python_data)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Teacher Data Created'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')
