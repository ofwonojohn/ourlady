from .models import ALevelMark, ALevelStudentProfile
from core.models import Term

MAIN_SUBJECT_GRADING = [
    (85, 'A', 6),
    (70, 'B', 5),
    (60, 'C', 4),
    (50, 'D', 3),
    (0, 'F', 0),
]

SUBSIDIARY_SUBJECTS = ['General Paper', 'Subsidiary Mathematics', 'Subsidiary ICT']
SUBSIDIARY_POINTS = lambda score: 1 if score >= 50 else 0


def grade_main_subject(score):
    for threshold, grade, points in MAIN_SUBJECT_GRADING:
        if score >= threshold:
            return grade, points
    return 'F', 0


def grade_subsidiary(score):
    return '1 Point' if score >= 50 else '0 Point'


def calculate_student_points(student, term: Term):
    try:
        profile = student.alevelstudentprofile
        combination_subjects = profile.combination.subjects.all()
    except ALevelStudentProfile.DoesNotExist:
        return {
            'error': 'Student profile not found.',
            'total_points': 0,
            'details': []
        }

    # Fetch marks
    marks = ALevelMark.objects.filter(student=student, term=term)
    details = []
    total_points = 0

    # Handle main subjects
    for mark in marks:
        if mark.subject in combination_subjects:
            grade, points = grade_main_subject(mark.score)
            total_points += points
            details.append({
                'subject': mark.subject.name,
                'score': mark.score,
                'grade': grade,
                'points': points,
                'type': 'Main'
            })

    # General Paper
    gp_mark = marks.filter(subject__name='General Paper').first()
    if gp_mark:
        gp_point = SUBSIDIARY_POINTS(gp_mark.score)
        total_points += gp_point
        details.append({
            'subject': 'General Paper',
            'score': gp_mark.score,
            'grade': grade_subsidiary(gp_mark.score),
            'points': gp_point,
            'type': 'Subsidiary'
        })

    # Subsidiary Subject: decide based on combo
    combo_subject_names = [sub.name for sub in combination_subjects]
    if 'Mathematics' in combo_subject_names or 'Entrepreneurship' in combo_subject_names:
        sub_name = 'Subsidiary ICT'
    else:
        sub_name = 'Subsidiary Mathematics'

    sub_mark = marks.filter(subject__name=sub_name).first()
    if sub_mark:
        sub_point = SUBSIDIARY_POINTS(sub_mark.score)
        total_points += sub_point
        details.append({
            'subject': sub_name,
            'score': sub_mark.score,
            'grade': grade_subsidiary(sub_mark.score),
            'points': sub_point,
            'type': 'Subsidiary'
        })

    return {
        'total_points': total_points,
        'details': details
    }
