from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_safe
from chats.models import Chat


@csrf_exempt
@require_safe
def chats_list(request):
    chats = Chat.objects.all().values('topic')
    return JsonResponse({
        'chats': list(chats)
      })


@csrf_exempt
@require_safe
def chat_page(request, pk):
    return JsonResponse({
        'message1': 'message_id123',
        'message2': 'message_id124',
        'message3': 'message_id125',
    })


@csrf_exempt
@require_safe
def index(request):
    return render(request, 'index.html')


@require_safe
def create_chat(request, topic):
    chat = Chat.objects.create(topic=topic)
    return JsonResponse({
        'created': chat.id
    })
