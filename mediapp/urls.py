from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/',views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),

]