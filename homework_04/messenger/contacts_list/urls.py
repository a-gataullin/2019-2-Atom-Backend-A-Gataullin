from contacts_list.views import contacts_list
from django.urls import path

urlpatterns = [
    path('<str:pk>', contacts_list, name='contacts_list'),
]
