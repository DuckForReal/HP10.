from django.urls import path
from . import views
app_name = 'destination'

urlpatterns = [
    path('', views.destination_list, name='destination_list'),
    path('create/', views.destination_create, name='destination_create'),
    path('<slug:slug>/', views.destination_detail, name='destination_detail'),
    path('<slug:slug>/edit/', views.destination_edit, name='destination_edit'),
    path('<slug:slug>/delete/', views.destination_delete, name='destination_delete'),
]