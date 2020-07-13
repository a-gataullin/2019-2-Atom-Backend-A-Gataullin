from django.http import JsonResponse


def user_profile(request, pk):
    if request.method == 'GET':
        return JsonResponse({'profile_of_user': pk})
    return JsonResponse({'Error': 'Method not allowed'}, status=405)
