from django.http import JsonResponse
from django.shortcuts import render


def chat_list(request, pk):
    if request.method == 'GET':
        return JsonResponse({'test': 'App'})


def index(request):
    return render(request, 'index.html')
