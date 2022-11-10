# Generated by Django 4.1.2 on 2022-11-10 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university_app', '0015_alter_address_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='liste_of_tools',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='personel_email',
        ),
        migrations.AddField(
            model_name='session',
            name='list_of_tools',
            field=models.CharField(choices=[('software tools', 'software tools'), ('hardware tools', 'hardware tools')], db_column='list of tools', default='software tools', max_length=100),
        ),
        migrations.AddField(
            model_name='teacher',
            name='personal_email',
            field=models.EmailField(db_column='personal email', default='<empty>', max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='university_app.student'),
        ),
    ]