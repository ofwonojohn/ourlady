from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def register_student(request):
    # Your registration logic here
    return render(request, 'register_student.html')

def add_mark(request):
    return render(request,'add_mark.html')

def view_results(request):
    return render(request,'view_results.html')