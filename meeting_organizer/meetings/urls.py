from django.urls import path
from . import views

urlpatterns = [
    path('', views.meeting_list, name='meeting_list'),
    path('edit/<int:pk>/', views.meeting_edit, name='meeting_edit'),
    path('add_meeting/', views.add_meeting, name='add_meeting'),
    path('meeting_list/', views.meeting_list, name='meeting_list'),
    path('get_meeting_details/<int:meeting_id>/', views.get_meeting_details, name='get_meeting_details'),
    path('delete_meeting/', views.delete_meeting, name='delete_meeting'),
    path('update_meeting/', views.update_meeting, name='update_meeting'),
]
