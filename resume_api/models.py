from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime


# @dataclass
# class Award:
#     name: str
#     description: str
#     project_date: Optional[datetime] = None
#     link: Optional[str] = None
#
#
# @dataclass
class Education(models.Model):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, related_name='education',
                               help_text='The resume the education is associated with')
    name = models.CharField(max_length=200, help_text="The name of educational institution")
    completion_date = models.DateField(help_text="The actual or expected completion date")
    gpa = models.FloatField(null=True, help_text="The GPA, if applicable")
    degree = models.CharField(max_length=200, null=True, help_text="The degree or certificate, if applicable")
    major = models.CharField(max_length=200, null=True, help_text="The major, if applicable")
    coursework = models.TextField(null=True, help_text="The coursework, if applicable")
#
#
# @dataclass
# class SkillCategory:
#     name: str
#     skills: List[str]
#
#
# @dataclass
# class Work:
#     name: str
#     location: str
#     start_date: datetime
#     description: str
#     end_date: Optional[datetime] = None


class Resume(models.Model):
    user = models.ForeignKey(User, help_text='The user that owns the resume', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, help_text="The name of the resume owner")
    contact_email = models.EmailField(help_text="The email that will appear on the resume")
    contact_phone = models.CharField(max_length=15)
    # education: List[Education]
    # projects: List[Award]
    # work: List[Work]
    # awards: List[Award]
    # skill_categories: List[SkillCategory]
    #     links: List[str]


    def __str__(self):
        return f"{self.user}'s Resume (#{self.id})"
