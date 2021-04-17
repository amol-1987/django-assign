from django.conf.urls import url, include
from django.contrib import admin
from app1 import views
urlpatterns = [
    path('tasklist/', views.tasklist, name='list'),
    path('taskdetail/<str:pk>', views.taskdetail, name="detail"),
    
    
]
