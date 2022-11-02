import datetime

from django.db import models


class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(default='', max_length=100, null=False, blank=False, db_column='name')
    familyName = models.CharField(default='', max_length=100, null=False, blank=False, db_column='family Name')
    personel_email = models.EmailField(default='', max_length=100, null=False, blank=False, db_column='personel email')
    work_email = models.EmailField(default='', max_length=100, null=False, blank=False, db_column='work email')
    total_hours_per_week = models.IntegerField(default=0, null=False, blank=False, db_column='total hours per week')
    photo = models.ImageField(default='', null=False, blank=False, db_column='photo')

    modules = models.ManyToManyField('Module', through='ModuleTeacher', related_name='teachers')
    groupe = models.ManyToManyField('Groupe', through='GroupeTeacher', related_name='teachers')


class Groupe(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(default='', max_length=100, null=False, blank=False, db_column='name')
    numberOfStudents = models.IntegerField(default=0, blank=False, db_column='number Of Students')
    email = models.EmailField(default='', max_length=100, null=False, blank=False, db_column='email')
    level = models.CharField(default='', max_length=100, null=False, blank=False, db_column='level')
    module = models.ManyToManyField('Module', through='ModuleGroupe', related_name='groups')


class Student(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(default='', max_length=100, null=False, blank=False, db_column='name')
    familyName = models.CharField(default='', max_length=100, null=False, blank=False, db_column='family Name')
    birthday = models.DateField(datetime.date.today(), db_column='birthday')
    photo = models.ImageField(default='', null=False, blank=False, db_column='photo')
    state = models.CharField(default='', max_length=100, null=False, blank=False, db_column='state', choices=(
        ('present', 'present'),
        ('absent', 'absent'),
        ('delayed', 'delayed'),
        ('excluded', 'excluded'),
    ))
    situation = models.CharField(default='', max_length=100, null=False, blank=False, db_column='situation', choices=(
        ('new', 'new'),
        ('repeating', 'repeating'),
        ('derogatory', 'derogatory'),
        ('other', 'other'),
    ))

    groupe = models.ForeignKey('Groupe', on_delete=models.CASCADE, related_name='student')


class List_Of_Absence(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField(datetime.date.today(), db_column='date')
    motif = models.CharField(default='', max_length=100, db_column='motif')
    justification = models.CharField(default='', max_length=100, db_column='justification')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, default=0, db_column='student')


class Session(models.Model):
    id = models.IntegerField(primary_key=True)
    start_date = models.DateField(datetime.date.today(), db_column='start date')
    end_date = models.DateField(datetime.date.today(), db_column='end date')
    classroom_number = models.IntegerField(db_column='classroom number')
    goal = models.CharField(default='', max_length=1000, db_column='goal')
    summary = models.CharField(default='', max_length=1000, db_column='summary')
    liste_of_tools = models.CharField(default='', max_length=100, db_column='liste of tools', choices=(
        ('software tools', 'software tools'),
        ('hardware tools', 'hardware tools'),
    ))
    module = models.ForeignKey('Module', on_delete=models.CASCADE, null=False, default=0, db_column='module')
    state = models.CharField(default='', max_length=100, null=False, blank=False, db_column='state', choices=(
        ('running', 'running'),
        ('achieved', 'achieved'),
        ('cancelled', 'cancelled'),
        ('delayed', 'delayed'),
    ))
    type = models.CharField(default='', max_length=100, null=False, blank=False, db_column='type', choices=(
        ('normal', 'normal'),
        ('catch-up', 'catch-up'),
        ('support', 'support'),
        ('training', 'training'),
    ))


class Module(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(default='', max_length=100, null=False, blank=False, db_column='name', unique=True)
    nbHours = models.IntegerField(default=0, blank=False, db_column='number Of Hours')
    type = models.CharField(default='', max_length=100, null=False, blank=False, db_column='type', choices=(
        ('optional', 'optional'),
        ('required', 'required'),
    ))
    study_level = models.CharField(default='', max_length=100, null=False, blank=False, db_column='study level')
    sessions = models.ManyToManyField(Session, through='ModuleSession', related_name='modules')


class ModuleTeacher(models.Model):
    id = models.IntegerField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False, default=0, db_column='teacher')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=False, default=0, db_column='module')


class ModuleGroupe(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(Groupe, on_delete=models.CASCADE, null=False, default=0, db_column='group')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=False, default=0, db_column='module')


class ModuleSession(models.Model):
    id = models.IntegerField(primary_key=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=False, default=0, db_column='session')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=False, default=0, db_column='module')


class GroupeTeacher(models.Model):
    id = models.IntegerField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False, default=0, db_column='teacher')
    group = models.ForeignKey(Groupe, on_delete=models.CASCADE, null=False, default=0, db_column='group')
