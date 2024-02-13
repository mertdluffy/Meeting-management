from django.urls import path
from . import views

urlpatterns = [
    path('', views.meeting_list, name='meeting_list'),
    path('edit/<int:pk>/', views.meeting_edit, name='meeting_edit'),
    path('add_meeting/', views.add_meeting, name='add_meeting'),
    path('meeting_list/', views.meeting_list, name='meeting_list'),
]
