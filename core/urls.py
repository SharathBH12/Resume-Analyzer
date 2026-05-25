from django.contrib import admin
from django.urls import path

from analyzer import views


urlpatterns = [

    # Admin Panel
    path('admin/', admin.site.urls),

    # Home Page
    path('', views.home, name='home'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Resume Analyzer
    path('upload/', views.upload_resume, name='upload'),
]