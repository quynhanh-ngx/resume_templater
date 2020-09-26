from .models import Resume, Education, Project, Link, Skill, Work
from .serializers import ResumeSerializer, EducationSerializer, \
    ProjectSerializer, LinkSerializer, SkillSerializer, WorkSerializer
from rest_framework import generics


class ResumeListCreate(generics.ListCreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class EducationListCreate(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class LinkListCreate(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class SkillListCreate(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class WorkListCreate(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
