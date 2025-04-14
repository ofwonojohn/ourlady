from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_student, name='register_student'),
    path('add-mark/', views.add_mark, name='add_mark'),
    path('view_results', views.view_results, name='view_results')
]
