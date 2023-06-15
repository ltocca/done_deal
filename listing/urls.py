from django.urls import path
from . import views

app_name = 'listing'

urlpatterns = [
    path('<int:pk>', views.detail, name='detail'),
    path('new/', views.new_listing, name='new_listing'),
    path('<int:pk>/edit_listing/', views.edit_listing, name='edit'),
    path('<int:pk>/delete/', views.delete_listing, name='delete_listing'),

    # TODO: fix redirect from delete
]
