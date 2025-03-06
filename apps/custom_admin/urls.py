from django.urls import path,include
from apps.custom_admin import views

urlpatterns = [

# path('', views.dashboard, name='admin_dashboard'),
    path('', views.dashboard, name='admin_dashboard'),
    path('login/', views.custom_login, name='custom_login'),
    path('logout/', views.custom_logout, name='logout'),

]
