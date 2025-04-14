from django.db import models

class ClassLevel(models.Model):
    LEVEL_CHOICES = [
        ('S1', "Senior 1"),
        ('S2', "Senior 2"),
        ('S3', "Senior 3"),
        ('S4', "Senior 4"),
        ('S5', "Senior 5"),
        ('S6', "Senior 6"),
    ]
    name = models.CharField(max_length=2, choices=LEVEL_CHOICES, unique=True)

    def __str__(self):
        return dict(self.LEVEL_CHOICES).get(self.name, self.name)


class Student(models.Model):
    EDUCATION_LEVELS = [
        ('O', "O'Level"),
        ('A', "A'Level"),
    ]

    name = models.CharField(max_length=100)
    dob = models.DateField()
    education_level = models.CharField(max_length=1, choices=EDUCATION_LEVELS)
    class_level = models.ForeignKey(ClassLevel, on_delete=models.CASCADE)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Term(models.Model):
    name = models.CharField(max_length=10)  # e.g. "Term 1"
    year = models.IntegerField()

    class Meta:
        unique_together = ('name', 'year')

    def __str__(self):
        return f"{self.name} {self.year}"
