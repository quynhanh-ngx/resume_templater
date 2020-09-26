from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('resume/', views.ResumeListCreate.as_view()),
    path('education/', views.EducationListCreate.as_view()),
    path('skills/', views.SkillListCreate.as_view()),
    path('work/', views.WorkListCreate.as_view()),
    path('links/', views.LinkListCreate.as_view()),
    path('projects/', views.ProjectListCreate.as_view()),
    path('api/token-auth/', obtain_jwt_token),
    path('api/current-user/', views.current_user),
    path('api/users/', views.UserList.as_view()),
]
