from django.urls import path
from . import views
from .views import driver_dashboard

urlpatterns = [
    path("", views.index, name='home'),
    path("home", views.index, name='home'),
    path('about/', views.about, name='about'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('user/login/', views.login_view, name='user_login'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('bill/', views.order, name='bill'),
    path('contact/', views.contact, name='contact'),
    path('driver/dashboard/', views.driver_dashboard, name='driver_dashboard'),
path('update-task-status/<int:id>/', views.update_task_status, name='update_task_status'),

]
