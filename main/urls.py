from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('sign', views.sign, name='sign'),
    path("enteruser/", views.enteruser, name='enteruser'),
    path("createuser/", views.createuser, name='createuser'),

    path('api/user/', views.user, name='api_user'),
    # path('api/subject/', views.subject, name='api_subject'),
    # path('api/group/', views.group, name='api_group'),
    # path('api/progress/', views.progress, name='api_progress'),
    path('api/student/subjects/', views.get_student_subjects, name='api_get_student_subjects'),
    path('api/professor/groups/', views.get_professor_groups, name='api_get_professor_groups'),
]
