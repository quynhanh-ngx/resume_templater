from django.contrib import admin

from resume_api import models

# Register your models here.
@admin.register(models.Resume)
class ResumeAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
    pass
