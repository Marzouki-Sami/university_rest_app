import django.utils.timezone
from django.db import models

student_states = (
    ('present', 'present'),
    ('absent', 'absent'),
    ('delayed', 'delayed'),
    ('excluded', 'excluded'),
)

student_situation = (
    ('new', 'new'),
    ('repeating', 'repeating'),
    ('derogatory', 'derogatory'),
    ('other', 'other'),
)

list_of_tools = (
    ('software tools', 'software tools'),
    ('hardware tools', 'hardware tools'),
)

session_states = (
    ('running', 'running'),
    ('achieved', 'achieved'),
    ('cancelled', 'cancelled'),
    ('delayed', 'delayed'),
)

session_types = (
    ('normal', 'normal'),
    ('catch-up', 'catch-up'),
    ('support', 'support'),
    ('training', 'training'),
)

module_types = (
    ('optional', 'optional'),
    ('required', 'required'),
)


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default='<empty>', max_length=100, null=False, blank=False, db_column='name')
    familyName = models.CharField(default='<empty>', max_length=100, null=False, blank=False, db_column='family Name')
    photo = models.ImageField(default='<empty>', null=False, blank=False, db_column='photo')
    birthday = models.DateField(default=django.utils.timezone.now, null=False, blank=False, db_column='birthday')

    class Meta:
        abstract = True


class Teacher(Person):
    grade = models.IntegerField(default=0, null=False, blank=False, db_column='grade')
    personal_email = models.EmailField(default='<empty>', max_length=100, null=False, blank=False,
                                       db_column='personal email')
    work_email = models.EmailField(default='<empty>', max_length=100, null=False, blank=False, db_column='work email')
    total_hours_per_week = models.IntegerField(default=0, null=False, blank=False, db_column='total hours per week')
    modules = models.ManyToManyField('Module', through='ModuleTeacher', related_name='teachers')
    groupe = models.ManyToManyField('Groupe', through='GroupeTeacher', related_name='teachers')

    class Meta:
        db_table = 'teacher'

    def __str__(self):
        return self.name


class Groupe(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(default='<empty>', max_length=100, null=False, blank=False, db_column='name')
    numberOfStudents = models.IntegerField(default=0, blank=False, db_column='number Of Students')
    email = models.EmailField(default='<empty>', max_length=100, null=False, blank=False, db_column='email')
    level = models.CharField(default='<empty>', max_length=100, null=False, blank=False, db_column='level')
    module = models.ManyToManyField('Module', through='ModuleGroupe', related_name='groups')

    class Meta:
        db_table = 'groupe'

    def __str__(self):
        return self.name


class Address(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.IntegerField(default=0, null=False, blank=False, db_column='number')
    street = models.CharField(default='<empty>', max_length=100, null=False, blank=False, db_column='street')
    city = models.CharField(default='<empty>', max_length=100, null=False, blank=False, db_column='city')
    postal_code = models.IntegerField(default=0, null=False, blank=False, db_column='postal code')
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='address')

    class Meta:
        db_table = 'address'

    def __str__(self):
        return self.city


class Student(Person):
    state = models.CharField(default=student_states[0][0], max_length=100, null=False, blank=False, db_column='state',
                             choices=student_states)
    situation = models.CharField(default=student_situation[0][0], max_length=100, null=False, blank=False,
                                 db_column='situation', choices=student_situation)
    groupe = models.ForeignKey('Groupe', on_delete=models.CASCADE, related_name='student')

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.name


class ListOfAbsence(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField(django.utils.timezone.now, db_column='date')
    motif = models.CharField(default='<empty>', max_length=100, db_column='motif')
    justification = models.CharField(default='<empty>', max_length=100, db_column='justification')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, default=0, db_column='student')

    class Meta:
        db_table = 'list of absence'


class Session(models.Model):
    id = models.IntegerField(primary_key=True)
    start_date = models.DateField(django.utils.timezone.now, db_column='start date')
    end_date = models.DateField(django.utils.timezone.now, db_column='end date')
    classroom_number = models.IntegerField(db_column='classroom number')
    goal = models.CharField(default='<empty>', max_length=1000, db_column='goal')
    summary = models.CharField(default='<empty>', max_length=1000, db_column='summary')
    list_of_tools = models.CharField(default=list_of_tools[0][0], max_length=100, db_column='list of tools',
                                     choices=list_of_tools)
    module = models.ForeignKey('Module', on_delete=models.CASCADE, null=False, default=0, db_column='module')
    state = models.CharField(default=session_states[0][0], max_length=100, null=False, blank=False, db_column='state',
                             choices=session_states)
    type = models.CharField(default=session_types[0][0], max_length=100, null=False, blank=False, db_column='type',
                            choices=session_types)

    class Meta:
        db_table = 'session'

    def __str__(self):
        return self.goal


class Module(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(default='<empty>', max_length=100, null=False, blank=False, db_column='name', unique=True)
    nbHours = models.IntegerField(default=0, blank=False, db_column='number Of Hours')
    type = models.CharField(default=module_types[0][0], max_length=100, null=False, blank=False, db_column='type',
                            choices=module_types)
    study_level = models.CharField(default='<empty>', max_length=100, null=False, blank=False, db_column='study level')
    sessions = models.ManyToManyField(Session, through='ModuleSession', related_name='modules')

    class Meta:
        db_table = 'module'


class ModuleTeacher(models.Model):
    id = models.IntegerField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False, default=0, db_column='teacher')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=False, default=0, db_column='module')

    class Meta:
        db_table = 'module teacher association'


class ModuleGroupe(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(Groupe, on_delete=models.CASCADE, null=False, default=0, db_column='group')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=False, default=0, db_column='module')

    class Meta:
        db_table = 'module group association'


class ModuleSession(models.Model):
    id = models.IntegerField(primary_key=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=False, default=0, db_column='session')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=False, default=0, db_column='module')

    class Meta:
        db_table = 'module session association'


class GroupeTeacher(models.Model):
    id = models.IntegerField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False, default=0, db_column='teacher')
    group = models.ForeignKey(Groupe, on_delete=models.CASCADE, null=False, default=0, db_column='group')

    class Meta:
        db_table = 'group teacher association'
