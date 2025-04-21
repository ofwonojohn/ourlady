from django.db import models

class Subject(models.Model):
    SUBJECT_TYPE_CHOICES = (
        ('main', 'Main Subject'),
        ('subsidiary', 'Subsidiary Subject'),
        ('compulsory', 'Compulsory Subject'),
    )

    name = models.CharField(max_length=100)
    subject_type = models.CharField(max_length=20, choices=SUBJECT_TYPE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.subject_type})"


class SubjectCombination(models.Model):
    name = models.CharField(max_length=100)
    main_subjects = models.ManyToManyField(Subject, limit_choices_to={'subject_type': 'main'})

    def __str__(self):
        return self.name


class Student(models.Model):
    LEVEL_CHOICES = (
        ('S5', 'Senior 5'),
        ('S6', 'Senior 6'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    combination = models.ForeignKey(SubjectCombination, on_delete=models.CASCADE)
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    year = models.PositiveIntegerField()

    subsidiary_subjects = models.ManyToManyField(
        Subject,
        limit_choices_to={'subject_type': 'subsidiary'},
        blank=True,
        related_name='subsidiary_students'
    )
    compulsory_subjects = models.ManyToManyField(
        Subject,
        limit_choices_to={'subject_type': 'compulsory'},
        blank=True,
        related_name='compulsory_students'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.grade}"
