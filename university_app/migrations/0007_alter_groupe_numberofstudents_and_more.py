# Generated by Django 4.1.2 on 2022-10-27 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university_app', '0006_alter_groupe_name_alter_groupe_numberofstudents_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupe',
            name='numberOfStudents',
            field=models.IntegerField(db_column='number Of Students', default=0),
        ),
        migrations.AlterField(
            model_name='groupe',
            name='numberOfTeachers',
            field=models.IntegerField(db_column='number Of Teachers', default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='familyName',
            field=models.CharField(db_column='family Name', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='familyName',
            field=models.CharField(db_column='family Name', default='', max_length=100),
        ),
    ]
