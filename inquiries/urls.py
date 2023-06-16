
from django.urls import path

from . import views

app_name = 'inquiry'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.chat, name='chat'),
    path('new_chat/<int:listing_pk>/', views.new_chat, name='new_chat'),
]
