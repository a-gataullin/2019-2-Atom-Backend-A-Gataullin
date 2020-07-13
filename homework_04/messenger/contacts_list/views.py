from django.http import JsonResponse


def contacts_list(request, pk):
    if request.method == 'GET':
        return JsonResponse({'contacts_list_of': pk})
