from chats.views import chats_list, chat_page, create_chat
from django.urls import path

urlpatterns = [
    path('', chats_list, name='chats_list'),
    path('<int:pk>', chat_page, name='chat_page'),
    path('create/<str:topic>', create_chat, name='create_chat')
]
