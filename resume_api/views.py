from django.shortcuts import render

from .models import Resume, Education
from .serializers import ResumeSerializer, EducationSerializer
from rest_framework import generics

# Create your views here.

class ResumeListCreate(generics.ListCreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class EducationListCreate(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
