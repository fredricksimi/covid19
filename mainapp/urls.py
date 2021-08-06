from django.urls import path
from . import views

app_name="mainapp"
urlpatterns = [
    path('', views.home_view, name='homepage'),
    path('seven', views.seven_days, name='seven'),
    path('emails', views.view_emails, name='emails'),
    path('delete/<int:id>/', views.delete_email, name='delete-email')
]
