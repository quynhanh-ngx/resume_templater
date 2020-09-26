from rest_framework import serializers
from .models import Resume, Education


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('user', 'name', 'contact_email', 'contact_phone')


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('resume',
                  'name',
                  'completion_date',
                  'gpa',
                  'degree',
                  'major',
                  'coursework',)
