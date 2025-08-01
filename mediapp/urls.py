from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/',views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('diagnosis/', views.diagnosis, name='diagnosis'),

    path('family/', views.family, name='family'),
    path('doctors/', views.doctors, name='doctors'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('add_family/', views.add_family, name='add_family'),
   
    path('predict/', views.predict_heart_disease, name='predict_heart_disease'),

    path('ai_diagnosis0/', views.ai_diagnosis0, name='ai_diagnosis0'),
    path('ai_diagnosis1/', views.ai_diagnosis1, name='ai_diagnosis1'),
    path('ai_diagnosis2/', views.ai_diagnosis2, name='ai_diagnosis2'),
    path('ai_diagnosis3/', views.ai_diagnosis3, name='ai_diagnosis3 '),
]