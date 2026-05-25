from django.contrib import admin
from django.urls import path
from analyzer import views

urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('register/', views.register, name='register'),

    path('login/', views.login_page, name='login'),

    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('upload/', views.upload_resume, name='upload'),

    path('logout/', views.logout_page, name='logout'),
]