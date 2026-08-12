from django.urls import path
from . import views

urlpatterns = [
    # Main homepage
    path('', views.home, name='home'),
    
    # Navigation pages
    path('latest/', views.latest_projects, name='latest_projects'), 
    path('fashion/', views.fashion_projects, name='fashion_projects'),
    path('rates/', views.rates_view, name='rates'),
    path('project/<int:pk>/', views.project_detail, name='project_detail')
]