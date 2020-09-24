from django.contrib import admin

from resume_api import models

# Register your models here.
@admin.register(models.Resume)
class ResumeAdmin(admin.ModelAdmin):
    pass
