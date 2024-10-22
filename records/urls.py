from django.urls import path
from . import views

urlpatterns = [
    path('', views.record_list, name='record_list'),
    path('new/', views.record_create, name='record_create'),
    path('<int:pk>/edit/', views.record_update, name='record_update'),
    path('<int:pk>/delete/', views.record_delet, name='record_delet'),
]