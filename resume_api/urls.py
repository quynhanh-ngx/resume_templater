from django.urls import path
from . import views

urlpatterns = [
    path('resume/', views.ResumeListCreate.as_view()),
    path('education/', views.EducationListCreate.as_view()),
    path('skills/', views.SkillListCreate.as_view()),
    path('work/', views.WorkListCreate.as_view()),
    path('links/', views.LinkListCreate.as_view()),
    path('projects/', views.ProjectListCreate.as_view()),
]
