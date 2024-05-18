from django.http import FileResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import *

def main(request):
    pass


def profile(request):
    user = request.user
    profile = Profile.objects.get(user_id = user)
    characteristic = Characteristic.objects.get(pk=profile.characteristic.pk)


    count_learned_words = characteristic.learned_words.count()

    last_tales = characteristic.last_completed_tales
    tale = last_tales.all_info_tales
    title = 'Профиль'

    context = {
        'title': title,
        'last_tale': tale,
        'progress_value': last_tales.percent_progress,
        'last_tale_name': tale.name_tales,
        'user': user,
        'profile': profile,
        'all_completed_lessons': characteristic.all_completed_lessons,
        'learned_words': count_learned_words,
        'completed_tales': characteristic.completed_tales,
    }
    return render(request, 'profile.html', context=context)


def tails_select(request):
    user = request.user
    profile = Profile.objects.get(user_id=user)
    characteristic = Characteristic.objects.get(pk=profile.characteristic.pk)

    tales_statistic = profile.tales_info_progress_id.all()
    print(tales_statistic)
    title = 'Выбор сказки'
    context = {
        'progress_value_1': tales_statistic[0].percent_progress,
        'progress_value_2': tales_statistic[1].percent_progress,
        'title': title,
    }
    return render(request, 'tails_select.html', context=context)

def get_image(request, image_id):
    profile = get_object_or_404(Profile, pk=image_id)
    image_path = profile.profile_image.path
    return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')

@csrf_exempt
@require_POST
def upload_avatar(request):
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({'error': 'Зрегестрируйтесь.'}, status=403)

    profile = get_object_or_404(Profile, user=user)
    if 'avatar' in request.FILES:
        profile.profile_image = request.FILES['avatar']
        profile.save()
        return JsonResponse({'status': 'success', 'image_url': profile.profile_image.url})

    return JsonResponse({'error': 'No file uploaded.'}, status=400)

def update_username(request):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({'error': 'Зрегестрируйтесь.'}, status=403)

    if 'username' in request.POST:
        user.username = request.POST['username']
        user.save()
        return JsonResponse({'status': 'success', 'username': user.username})

def main_page(request):
    return render(request, 'main.html')