from django.urls import path
from . import views

app_name = 'listing'

urlpatterns = [
    path('<int:pk>', views.detail, name='detail'),
    path('edit_listing/<int:pk>', views.edit, name='edit'),
    path('new/', views.new_listing, name='new_listing'),
    path('delete_listing/<int:pk>', views.delete_listing, name='delete_listing'),

    # TODO: fix redirect from delete
]
