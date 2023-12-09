from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('sign', views.sign, name='sign'),
    #path('personal', views.personal, name='personal'),
    path("reguser/", views.reguser, name='reguser'),
    path("enteruser/", views.enteruser, name='enteruser'),
]