from django.db import models
from django.contrib.auth.models import User


class Education(models.Model):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, related_name='education',
                               help_text='The resume the education is associated with')
    name = models.CharField(max_length=200, help_text="The name of educational institution")
    completion_date = models.DateField(help_text="The actual or expected completion date")
    gpa = models.FloatField(null=True, help_text="The GPA, if applicable")
    degree = models.CharField(max_length=200, null=True, help_text="The degree or certificate, if applicable")
    major = models.CharField(max_length=200, null=True, help_text="The major, if applicable")
    coursework = models.TextField(null=True, help_text="The coursework, if applicable")

    def __str__(self):
        return f"Education {self.name} for {self.resume}"


class Skill(models.Model):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, related_name='skills', related_query_name='skill',
                               help_text='The resume the skill is associated with')
    name = models.CharField(max_length=200, help_text="The name of the skill")
    category = models.CharField(max_length=200, help_text="The category of the skill")

    def __str__(self):
        return f"Skill {self.name} in {self.category} for {self.resume}"


class Link(models.Model):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, related_name='links', related_query_name='link',
                               help_text='The resume the link is associated with')
    name = models.CharField(max_length=200, help_text="The name of the link")
    url = models.URLField(max_length=200, help_text="The url for the link")

    def __str__(self):
        return f"Link {self.name} for {self.resume}"


class Work(models.Model):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, related_name='work',
                               help_text='The resume the work is associated with')
    name = models.CharField(max_length=200, help_text="The name of the work")
    description = models.TextField(help_text="The description of the work")
    start_date = models.DateField(help_text="The start date of the work")
    end_date = models.DateField(null=True, help_text="The end date of the work, if applicable")
    location = models.DateField(null=True, help_text="The location of the work, if applicable")

    def __str__(self):
        return f"Work {self.name} for {self.resume}"


class Project(models.Model):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, related_name='projects',
                               related_query_name='project',
                               help_text='The resume the project is associated with')
    name = models.CharField(max_length=200, help_text="The name of the project")
    description = models.TextField(help_text="The description of the project")
    start_date = models.DateField(help_text="The start date of the project")
    end_date = models.DateField(null=True, help_text="The end date of the project, if applicable")
    location = models.DateField(null=True, help_text="The location of the project, if applicable")
    link = models.URLField(null=True, max_length=200, help_text="The url for the project")

    def __str__(self):
        return f"Project {self.name} for {self.resume}"


class Resume(models.Model):
    user = models.ForeignKey(User, help_text='The user that owns the resume', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, help_text="The name of the resume owner")
    contact_email = models.EmailField(help_text="The email that will appear on the resume")
    contact_phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user}'s Resume (#{self.id})"
