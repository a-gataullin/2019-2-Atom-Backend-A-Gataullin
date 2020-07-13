from django.http import JsonResponse, HttpResponse


def chat_page(request, pk):
    if request.method == 'GET':
        return JsonResponse({'page': str(pk)})
    else:
        return HttpResponse(status_code=405)
