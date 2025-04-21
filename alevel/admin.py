from django.contrib import admin
from .models import Student, Subject, Grade, SubjectCombination

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'combination', 'dob', 'level', 'year')
    list_filter = ('combination', 'year')
    search_fields = ('first_name', 'last_name')

@admin.register(SubjectCombination)
class SubjectCombinationAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)

admin.site.register(Subject)
admin.site.register(Grade)

