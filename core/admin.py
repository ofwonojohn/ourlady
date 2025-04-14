from django.contrib import admin
from .models import ClassLevel, Student, Subject

@admin.register(ClassLevel)
class ClassLevelAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'class_level', 'date_registered']
    list_filter = ['class_level']
    search_fields = ['name']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'level']
    list_filter = ['level']
