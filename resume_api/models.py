from django.db import models

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
# class Education:
#     name: str
#     grad_date: datetime
#     gpa: float
#     degree: str
#     major: str
#     coursework: List[str]
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
    name = models.CharField(max_length=200, help_text="The name of the resume owner")
    contact_email = models.EmailField(help_text="The email that will appear on the resume")
    contact_phone = models.CharField(max_length=15)
    # education: List[Education]
    # projects: List[Award]
    # work: List[Work]
    # awards: List[Award]
    # skill_categories: List[SkillCategory]
    #     links: List[str]
