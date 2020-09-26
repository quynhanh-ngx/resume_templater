from rest_framework import serializers
from .models import Resume, Education, Skill, Link, Work, Project


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
                  'coursework')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('resume',
                  'name',
                  'category')


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('resume',
                  'name',
                  'url')


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('resume',
                  'name',
                  'description',
                  'start_date',
                  'end_date',
                  'location')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('resume',
                  'name',
                  'description',
                  'start_date',
                  'end_date',
                  'location',
                  'link')
