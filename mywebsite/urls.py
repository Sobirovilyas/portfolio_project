from django.urls import path
from mywebsite import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('blog/', views.blog_index, name='blog_index'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/categories/<str:category>/', views.categories, name='categories'),
]
