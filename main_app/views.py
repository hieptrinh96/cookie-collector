from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cookie, IceCream
from .forms import ReviewForm
from django.views.generic import ListView, DetailView

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cookies_index(request):
  cookies = Cookie.objects.all()
  return render(request, 'cookies/index.html', {'cookies': cookies})

def cookies_detail(request, cookie_id):
  cookie = Cookie.objects.get(id=cookie_id)
  iceCream_cookie_doesnt_have = IceCream.objects.exclude(id__in = cookie.iceCream.all().values_list('id'))
  review_form = ReviewForm()
  return render(request, 'cookies/detail.html', {
    'cookie': cookie,
    'review_form': review_form,
    'iceCream': iceCream_cookie_doesnt_have
  })

def add_review(request, cookie_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.cookie_id = cookie_id
    new_review.save()
  return redirect('cookies_detail', cookie_id=cookie_id)

class CookieCreate(CreateView):
  model = Cookie
  fields = ['name', 'flavor', 'description', 'quantity']
  success_url = '/cookies/'

class CookieUpdate(UpdateView):
  model = Cookie
  fields = ['name', 'flavor', 'description', 'quantity']

class CookieDelete(DeleteView):
  model = Cookie
  success_url = '/cookies/'

class IceCreamCreate(CreateView):
  model = IceCream
  fields = '__all__'

class IceCreamList(ListView):
  model = IceCream

class IceCreamDetail(DetailView):
  model = IceCream

class IceCreamUpdate(UpdateView):
  model = IceCream
  fields = ['name', 'flavor']

class IceCreamDelete(DeleteView):
  model = IceCream
  success_url = '/iceCream/'

def assoc_iceCream(request, cookie_id, iceCream_id):
  Cookie.objects.get(id=cookie_id).iceCream.add(iceCream_id)
  return redirect('cookies_detail', cookie_id=cookie_id)