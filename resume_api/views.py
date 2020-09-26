from django.shortcuts import render

from .models import Resume
from .serializers import ResumeSerializer
from rest_framework import generics

# Create your views here.

class ResumeListCreate(generics.ListCreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

