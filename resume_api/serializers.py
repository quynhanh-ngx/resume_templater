from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from .models import Resume, Education, Skill, Link, Work, Project, ResumeImage

User = get_user_model()


class ResumeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeImage
        fields = ('resume', 'name', 'image')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')


class ResumeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

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
