from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cookie
from .forms import ReviewForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cookies_index(request):
  cookies = Cookie.objects.all()
  return render(request, 'cookies/index.html', {'cookies': cookies})

def cookies_detail(request, cookie_id):
  cookie = Cookie.objects.get(id=cookie_id)
  review_form = ReviewForm()
  return render(request, 'cookies/detail.html', {
    'cookie': cookie,
    'review_form': review_form
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
  fields = '__all__'
  success_url = '/cats/'

class CookieUpdate(UpdateView):
  model = Cookie
  fields = ['name', 'flavor', 'description', 'quantity']

class CookieDelete(DeleteView):
  model = Cookie
  success_url = '/cookies/'