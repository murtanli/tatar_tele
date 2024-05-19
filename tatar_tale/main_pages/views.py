from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import FileResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .models import *


@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.get(user_id=user)
    characteristic = Characteristic.objects.get(pk=profile.characteristic.pk)

    count_learned_words = characteristic.learned_words.count()

    user_progress_tales = TalesInfo.objects.filter(user=user)
    last_tale_info = user_progress_tales.first()
    tale = last_tale_info.all_info_tales
    title = 'Профиль'

    context = {
        'title': title,
        'last_tale': tale,
        'progress_value': last_tale_info.percent_progress,
        'last_tale_name': tale.name_tales,
        'user': user,
        'profile': profile,
        'all_completed_lessons': characteristic.all_completed_lessons,
        'learned_words': count_learned_words,
        'completed_tales': characteristic.completed_tales,
    }
    return render(request, 'profile.html', context=context)


def tails_select(request):
    if not request.user.is_authenticated:
        return render(request, 'reg.html')

    user = request.user
    profile = Profile.objects.get(user_id=user.id)
    characteristic = Characteristic.objects.get(pk=profile.characteristic.pk)

    tales_statistic = profile.tales_info_progress_id.all()
    print(tales_statistic)
    title = 'Выбор сказки'

    # Initialize progress values
    progress_skaz1 = 0
    progress_skaz2 = 0

    # Check if there are at least two progress records
    if len(tales_statistic) > 0:
        if tales_statistic[0].percent_progress is not None:
            progress_skaz1 = tales_statistic[0].percent_progress
    if len(tales_statistic) > 1:
        if tales_statistic[1].percent_progress is not None:
            progress_skaz2 = tales_statistic[1].percent_progress

    context = {
        'progress_value_1': progress_skaz1,
        'progress_value_2': progress_skaz2,
        'profile': profile,
        'title': title,
    }
    return render(request, 'tails_select.html', context=context)


def get_image(request, image_id):
    profile = get_object_or_404(Profile, pk=image_id)
    image_path = profile.profile_image.path

    try:
        return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')
    except FileNotFoundError:
        return HttpResponseNotFound("Изображение не найдено")

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


def sign_in(request):
    if request.method == 'POST':
        login_text = request.POST.get('login')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Создаем пользователя и сохраняем его
            user = User.objects.create_user(username=login_text, password=password)
            user.email = email
            user.save()

            # Создаем объекты TalesInfo для пользователя
            all_tales = AllInfoTales.objects.all()
            last_completed_tales = None
            for tale in all_tales:
                last_completed_tales = TalesInfo.objects.create(
                    all_info_tales=tale,
                    user=user
                )

            # Создаем объект Characteristic для пользователя
            characteristic = Characteristic.objects.create(
                last_completed_tales=last_completed_tales
            )

            # Создаем профиль пользователя
            profile = Profile.objects.create(
                user=user,
                email=email,
                characteristic=characteristic
            )

            messages.success(request, 'Регистрация прошла успешно!')

            # Аутентифицируем и логиним пользователя
            user_auth = authenticate(username=login_text, password=password)
            login(request, user_auth)

            return redirect('oprosnik')

        except Exception as e:
            messages.error(request, f'Ошибка регистрации: {str(e)}')

    return render(request, 'reg.html')

def auth(request):
    if request.method == 'POST':
        login_text = request.POST.get('login')
        password_text = request.POST.get('password')

        user = authenticate(username=login_text, password=password_text)

        if user is not None:
            login(request, user)
            messages.success(request, 'Авторизация прошла успешно!')
            return redirect('tails_select')
        else:
            messages.error(request, 'Ошибка авторизации, неправильно введен пароль либо логин')
            return redirect('tails_select')


    return render(request, 'auth.html')


def oprosnik(request):
    return render(request, 'opros.html')

def logout(request):
    auth_logout(request)
    return redirect('main')

def save_opros(request):
    if request.method == 'POST':
        pass
