from django.db import models
from core.models import Student, Term

class OLevelSubject(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class OLevelMark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, limit_choices_to={'education_level': 'O'})
    subject = models.ForeignKey(OLevelSubject, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    score = models.FloatField()

    class Meta:
        unique_together = ('student', 'subject', 'term')

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}: {self.score}"
