from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cookie, IceCream
from .forms import ReviewForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def cookies_index(request):
  cookies = Cookie.objects.filter(user=request.user)
  return render(request, 'cookies/index.html', {'cookies': cookies})

@login_required
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

class CookieCreate(LoginRequiredMixin, CreateView):
  model = Cookie
  fields = ['name', 'flavor', 'description', 'quantity']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class CookieUpdate(LoginRequiredMixin, UpdateView):
  model = Cookie
  fields = ['name', 'flavor', 'description', 'quantity']

class CookieDelete(DeleteView):
  model = Cookie
  success_url = '/cookies/'

class IceCreamCreate(LoginRequiredMixin, CreateView):
  model = IceCream
  fields = '__all__'

class IceCreamList(LoginRequiredMixin, ListView):
  model = IceCream

class IceCreamDetail(LoginRequiredMixin, DetailView):
  model = IceCream

class IceCreamUpdate(LoginRequiredMixin, UpdateView):
  model = IceCream
  fields = ['name', 'flavor']

class IceCreamDelete(LoginRequiredMixin, DeleteView):
  model = IceCream
  success_url = '/iceCream/'

@login_required
def assoc_iceCream(request, cookie_id, iceCream_id):
  Cookie.objects.get(id=cookie_id).iceCream.add(iceCream_id)
  return redirect('cookies_detail', cookie_id=cookie_id)

class Home(LoginView):
  template_name = 'home.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cookies_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {
    'form': form,
    'error_message': error_message,
  }
  return render(request, 'signup.html', context)