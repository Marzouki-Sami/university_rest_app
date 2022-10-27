import datetime

from django.db import models


class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(default='', max_length=100, null=False, blank=False, db_column='name')
    familyName = models.CharField(default='', max_length=100, null=False, blank=False, db_column='family Name')
    email = models.EmailField(default='', max_length=100, null=False, blank=False, db_column='email')


class Groupe(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(default='', max_length=100, null=False, blank=False, db_column='name')
    numberOfStudents = models.IntegerField(default=0, blank=False, db_column='number Of Students')
    numberOfTeachers = models.IntegerField(default=0, blank=False, db_column='number Of Teachers')


class Student(models.Model):

    groupe = models.OneToOneField(
        Groupe,
        on_delete=models.CASCADE,
        null=False,
        default=0,
        )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(default='', max_length=100, null=False, blank=False, db_column='name')
    familyName = models.CharField(default='', max_length=100, null=False, blank=False, db_column='family Name')
    birthday = models.DateField(datetime.date.today(), db_column='birthday')
    email = models.EmailField(default='', max_length=100, null=False, blank=False, db_column='email')
