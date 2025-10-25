from django.urls import path

from blog import views

urlspatterns = [
    path('', views.PostView.as_view(), name='home')
]