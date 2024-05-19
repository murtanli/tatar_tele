from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main'),
    path('profile/', profile, name='profile'),
    path('tails_select/', tails_select, name='tails_select'),
    path('get_image/<int:image_id>/', get_image, name='get_image'),
    path('upload_avatar/', upload_avatar, name='upload_avatar'),
    path('update-username/', update_username, name='update-username'),
    path('sign_in/', sign_in, name='sign_in'),
    path('auth/', auth, name='auth'),
    path('oprosnik/', oprosnik, name='oprosnik'),
    path('logout/', logout, name='logout'),
    path('save_opros/', save_opros, name='save_opros'),
]
