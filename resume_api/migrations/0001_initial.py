# Generated by Django 3.1.1 on 2020-09-26 04:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the resume owner', max_length=200)),
                ('contact_email', models.EmailField(help_text='The email that will appear on the resume', max_length=254)),
                ('contact_phone', models.CharField(max_length=15)),
                ('user', models.ForeignKey(help_text='The user that owns the resume', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of educational institution', max_length=200)),
                ('completion_date', models.DateField(help_text='The actual or expected completion date')),
                ('gpa', models.FloatField(help_text='The GPA, if applicable', null=True)),
                ('degree', models.CharField(help_text='The degree or certificate, if applicable', max_length=200, null=True)),
                ('major', models.CharField(help_text='The major, if applicable', max_length=200, null=True)),
                ('coursework', models.TextField(help_text='The coursework, if applicable', null=True)),
                ('resume', models.ForeignKey(help_text='The resume the education is associated with', on_delete=django.db.models.deletion.CASCADE, related_name='education', to='resume_api.resume')),
            ],
        ),
    ]
