from django.urls import path
from . import views

app_name = 'listing'

urlpatterns = [
    path('<int:pk>', views.detail, name='detail'),
    path('new/', views.new_listing, name='new_listing'),
]
