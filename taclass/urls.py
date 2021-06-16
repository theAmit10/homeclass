from django.urls import path
from . import views

urlpatterns = [
    path('classes', views.classes , name='classes'), 
    path('createclass', views.createclass, name='createclass'),
    path('subject', views.subject, name='subject')
]