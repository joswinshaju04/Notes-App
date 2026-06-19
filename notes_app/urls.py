from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('create_note/', views.create_note, name='create_note'),
    path('delete/<int:id>', views.delete_note, name='delete'),
    path('update/<int:id>', views.update_note, name='update'),
    path('logout/', views.logout_user, name='logout'),
]