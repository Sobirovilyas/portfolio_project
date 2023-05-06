from django.urls import path
from mywebsite import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<int:pk>/', views.project_detail, name='project_detail')
]
