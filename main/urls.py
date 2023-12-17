from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.main),
    path('sign', views.sign, name='sign'),
    path("enteruser/", views.enteruser, name='enteruser'),
    path("createuser/", views.createuser, name='createuser'),
    re_path(r'^journal/group_id=(?P<group_id>\d+)/subject_id=(?P<subject_id>\d+)/$', views.journal_view, name='journal'),

    path('api/user/', views.user, name='api_user'),
    path('api/create_markcell', views.create_markcell, name='create_markcell'),
    path('api/update_grade', views.update_grade, name='update_grade'),
    # path('api/subject/', views.subject, name='api_subject'),
    # path('api/group/', views.group, name='api_group'),
    # path('api/progress/', views.progress, name='api_progress'),
    path('api/student/subjects/', views.get_student_subjects, name='api_get_student_subjects'),
    path('api/professor/groups/', views.get_professor_groups, name='api_get_professor_groups'),

]
