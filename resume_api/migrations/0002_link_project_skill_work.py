# Generated by Django 3.1.1 on 2020-09-26 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the work', max_length=200)),
                ('description', models.TextField(help_text='The description of the work')),
                ('start_date', models.DateField(help_text='The start date of the work')),
                ('end_date', models.DateField(help_text='The end date of the work, if applicable', null=True)),
                ('location', models.DateField(help_text='The location of the work, if applicable', null=True)),
                ('resume', models.ForeignKey(help_text='The resume the work is associated with', on_delete=django.db.models.deletion.CASCADE, related_name='work', to='resume_api.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the skill', max_length=200)),
                ('category', models.CharField(help_text='The category of the skill', max_length=200)),
                ('resume', models.ForeignKey(help_text='The resume the skill is associated with', on_delete=django.db.models.deletion.CASCADE, related_name='skills', related_query_name='skill', to='resume_api.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the project', max_length=200)),
                ('description', models.TextField(help_text='The description of the project')),
                ('start_date', models.DateField(help_text='The start date of the project')),
                ('end_date', models.DateField(help_text='The end date of the project, if applicable', null=True)),
                ('location', models.DateField(help_text='The location of the project, if applicable', null=True)),
                ('link', models.URLField(help_text='The url for the project', null=True)),
                ('resume', models.ForeignKey(help_text='The resume the project is associated with', on_delete=django.db.models.deletion.CASCADE, related_name='projects', related_query_name='project', to='resume_api.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the link', max_length=200)),
                ('url', models.URLField(help_text='The url for the link')),
                ('resume', models.ForeignKey(help_text='The resume the link is associated with', on_delete=django.db.models.deletion.CASCADE, related_name='links', related_query_name='link', to='resume_api.resume')),
            ],
        ),
    ]
