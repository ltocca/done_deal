
from django.urls import path

from . import views

app_name = 'inquiry'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new_chat/<int:item_pk>/', views.new_chat, name='new'),
]