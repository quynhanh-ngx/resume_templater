from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Resume, Education, Project, Link, Skill, Work, ResumeImage
from .serializers import ResumeSerializer, EducationSerializer, \
    ProjectSerializer, LinkSerializer, SkillSerializer, WorkSerializer, UserSerializerWithToken, \
    ResumeImageSerializer


User = get_user_model()


class ResumeListCreate(generics.ListCreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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

class ResumeImageListCreate(generics.ListCreateAPIView):
    queryset = ResumeImage.objects.all()
    serializer_class = ResumeImageSerializer


@api_view(['GET'])
def current_user(request):
    user = request.user
    resumes = ResumeSerializer(Resume.objects.filter(user=user), many=True)
    return Response({
        'username': user.username,
        'resumes': resumes.data
    })


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
