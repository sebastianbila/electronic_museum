from django.http import JsonResponse
from django.shortcuts import render, redirect

from newsletter.models import Newsletter


def subscribe(request):
    if request.is_ajax():
        email = request.POST['email']
        print('Email' + email)
        if email != '':
            if not Newsletter.objects.filter(email=email).exists():
                print('Email: ' + email)
                obj = Newsletter.objects.create(email=email)
                obj.save()
                if obj:
                    return JsonResponse({'status': True})
                else:
                    return JsonResponse({'status': False})
            else:
                return JsonResponse({'status': False})
    return redirect('home:index')
