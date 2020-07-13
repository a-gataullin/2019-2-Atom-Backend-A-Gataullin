from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_safe
from users.models import User


@csrf_exempt
@require_safe
def user_profile(request, pk):
    return JsonResponse({
        'name': pk,
        'nickname': pk + str(2019),
    })


@csrf_exempt
@require_safe
def contacts_list(request):
    return JsonResponse({
        'user1': 'id123456',
        'user2': 'id123457',
        'user3': 'id123458',
    })


@csrf_exempt
@require_safe
def find_user(request, nickname):
    users = User.objects.filter(username__contains=nickname).values('name',
                                                                    'username',
                                                                    'nickname')
    return JsonResponse({
      'users': list(users)
    })
