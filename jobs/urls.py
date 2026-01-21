from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('jobs/', views.job_list_view, name='job_list'),
    path('jobs/<int:job_id>/', views.job_detail_view, name='job_detail'),
    path('recommendations/', views.recommend_jobs_view, name='recommendations'),
]
