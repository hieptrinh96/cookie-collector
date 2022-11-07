from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Cookie


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cookies_index(request):
  cookies = Cookie.objects.all()
  return render(request, 'cookies/index.html', {'cookies': cookies})

def cookies_detail(request, cookie_id):
  cookie = Cookie.objects.get(id=cookie_id)
  return render(request, 'cookies/detail.html', {'cookie': cookie})

class CookieCreate(CreateView):
  model = Cookie
  fields = '__all__'