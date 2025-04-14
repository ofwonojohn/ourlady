from django.shortcuts import render, get_object_or_404, redirect
from .models import ALevelMark, ALevelStudentProfile, ALevelSubject
from core.models import Student, Term
from .forms import ALevelMarkForm
from .utils import calculate_student_points

def student_list(request):
    students = Student.objects.filter(education_level='A')
    return render(request, 'alevel/student_list.html', {'students': students})


def student_profile(request, student_id):
    profile = get_object_or_404(ALevelStudentProfile, student__id=student_id)
    return render(request, 'alevel/profile.html', {'profile': profile})


def submit_mark(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = ALevelMarkForm(request.POST)
        if form.is_valid():
            mark = form.save(commit=False)
            mark.student = student
            mark.save()
            return redirect('alevel:student_list')
    else:
        form = ALevelMarkForm()
    return render(request, 'alevel/mark_form.html', {'form': form, 'student': student})


def student_results(request, student_id, term_id):
    student = get_object_or_404(Student, id=student_id)
    term = get_object_or_404(Term, id=term_id)
    results = calculate_student_points(student, term)
    return render(request, 'alevel/results.html', {'student': student, 'results': results})

