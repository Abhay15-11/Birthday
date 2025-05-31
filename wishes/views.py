from django.shortcuts import render
from django.http import JsonResponse
from .models import BirthdayWish

def birthday_card(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        photo = request.FILES.get('photo')
        if name and photo:
            wish = BirthdayWish.objects.create(name=name, photo=photo)
            return JsonResponse({
                'name': wish.name,
                'photo_url': wish.photo.url
            })
        return JsonResponse({'error': 'Invalid data'}, status=400)

    return render(request, 'wishes/index.html')
