from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('members/', views.member_list, name='member_list'),
    path('members/add/', views.member_create, name='member_create'),
    path('members/<int:pk>/edit/', views.member_update, name='member_update'),
    path('members/<int:pk>/delete/', views.member_delete, name='member_delete'),
    path('report/', views.report, name='report'),
]
