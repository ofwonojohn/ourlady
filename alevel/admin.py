from django.contrib import admin
from .models import ALevelMark, SubjectCombination, ALevelSubject, ALevelStudentProfile

@admin.register(ALevelMark)
class ALevelMarkAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'score', 'term', 'get_combination']
    list_filter = ['term', 'subject']
    search_fields = ['student__name']

    def get_combination(self, obj):
        try:
            return obj.student.alevelstudentprofile.combination.name
        except ALevelStudentProfile.DoesNotExist:
            return 'N/A'
    get_combination.short_description = 'Combination'


@admin.register(SubjectCombination)
class CombinationAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ['subjects']


@admin.register(ALevelSubject)
class ALevelSubjectAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(ALevelStudentProfile)
class ALevelStudentProfileAdmin(admin.ModelAdmin):
    list_display = ['student', 'combination']
