from django.conf import settings
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
import requests


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', context={
            'site_key': settings.RECAPTCHA_SITE_KEY,
        })
    elif request.method == 'POST':
        username = request.POST.get('username')
        magic_text = request.POST.get('magic_text')
        recaptcha_token = request.POST.get('g-recaptcha-response')

        print(username)
        print(magic_text)
        print(recaptcha_token)

        data = {
            'response': recaptcha_token,
            'secret': settings.RECAPTCHA_SECRET_KEY
        }
        resp = requests.post(
            'https://www.google.com/recaptcha/api/siteverify', data=data)
        result_json = resp.json()
        print(result_json)

        return HttpResponseRedirect(reverse('login'))
