from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.chat, name='chat'),
    path('send_message/', views.send_message, name='send_message'),
]
