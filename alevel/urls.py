from django.urls import path
from . import views

app_name = 'alevel'

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('profile/<int:student_id>/', views.student_profile, name='profile'),
    path('marks/<int:student_id>/add/', views.submit_mark, name='submit_mark'),
    path('results/<int:student_id>/<int:term_id>/', views.student_results, name='student_results'),
]
