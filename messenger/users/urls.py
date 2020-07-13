from users.views import user_profile, contacts_list, find_user
from django.urls import path

urlpatterns = [
    path('contacts', contacts_list, name='contacts_list'),
    path('<str:pk>', user_profile, name='user_profile'),
    path('find/<str:nickname>', find_user, name='find_user')
]
