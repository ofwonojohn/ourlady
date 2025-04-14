from django.db import models
from core.models import Student, Term

class ALevelSubject(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class SubjectCombination(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subjects = models.ManyToManyField(ALevelSubject)

    def __str__(self):
        return self.name


class ALevelStudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, limit_choices_to={'education_level': 'A'})
    combination = models.ForeignKey(SubjectCombination, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.combination.name}"


class ALevelMark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, limit_choices_to={'education_level': 'A'})
    subject = models.ForeignKey(ALevelSubject, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    score = models.FloatField()

    class Meta:
        unique_together = ('student', 'subject', 'term')

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}: {self.score}"
