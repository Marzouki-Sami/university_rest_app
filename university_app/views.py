from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import Student, Groupe, Module, Teacher, Address, Session
from .serializers import StudentSerializer, GroupeSerializer, ModuleSerializer, TeacherSerializer, AddressSerializer, \
    SessionSerializer
from rest_framework import viewsets


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = [
        "get",
        "post",
        "put",
        "patch",
        "delete",
        "head",
        "options",
        "trace",
    ]


class GroupeViewSet(viewsets.ModelViewSet):
    queryset = Groupe.objects.all()
    serializer_class = GroupeSerializer
    http_method_names = [
        "get",
        "post",
        "put",
        "patch",
        "delete",
        "head",
        "options",
        "trace",
    ]


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    http_method_names = [
        "get",
        "post",
        "put",
        "patch",
        "delete",
        "head",
        "options",
        "trace",
    ]


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    http_method_names = [
        "get",
        "post",
        "put",
        "patch",
        "delete",
        "head",
        "options",
        "trace",
    ]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    http_method_names = [
        "get",
        "post",
        "put",
        "patch",
        "delete",
        "head",
        "options",
        "trace",
    ]


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    http_method_names = [
        "get",
        "post",
        "put",
        "patch",
        "delete",
        "head",
        "options",
        "trace",
    ]


@api_view(["GET", "POST"])
def retrieve_or_add_student(request):
    if request.method == "GET":
        students = Student.objects.all()
        if len(students) == 0:
            return JsonResponse({"message": "No students found"}, status=204)
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@api_view(["PUT", "PATCH", "DELETE", "GET"])
def update_or_delete_or_retrieve_student(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        return JsonResponse({"error": "Student not found"}, status=404)
    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "PATCH":
        data = JSONParser().parse(request)
        serializer = StudentSerializer(student, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        student.delete()
        return JsonResponse({"message": "Student deleted successfully"}, status=200)
    elif request.method == "GET":
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data, status=200)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@api_view(["GET", "POST"])
def retrieve_or_add_groupe(request):
    if request.method == "GET":
        groupes = Groupe.objects.all()
        if len(groupes) == 0:
            return JsonResponse({"message": "No groupes found"}, status=204)
        serializer = GroupeSerializer(groupes, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = GroupeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@api_view(["PUT", "PATCH", "DELETE", "GET"])
def update_or_delete_or_retrieve_groupe(request, groupe_id):
    try:
        groupe = Groupe.objects.get(pk=groupe_id)
    except Groupe.DoesNotExist:
        return JsonResponse({"error": "Groupe not found"}, status=404)
    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = GroupeSerializer(groupe, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "PATCH":
        data = JSONParser().parse(request)
        serializer = GroupeSerializer(groupe, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        groupe.delete()
        return JsonResponse({"message": "Groupe deleted successfully"}, status=200)
    elif request.method == "GET":
        serializer = GroupeSerializer(groupe)
        return JsonResponse(serializer.data, status=200)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
