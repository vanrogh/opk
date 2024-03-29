from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('list/', views.list_docs, name='list_docs'),
    path('delete_student_docs/', views.delete_student_docs, name='delete_student_docs'),
]
