from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main, name='main'),
    path('profile/', profile, name='profile'),
    path('tails_select/', tails_select, name='tails_select'),
    path('get_image/<int:image_id>/', get_image, name='get_image'),
    path('upload_avatar/', upload_avatar, name='upload_avatar'),
    path('update-username/', update_username, name='update-username'),
]
