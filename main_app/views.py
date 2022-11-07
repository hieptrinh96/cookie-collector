from django.shortcuts import render
from .models import Cookie

# Create your views here.

# Add the Cat class & list and view function below the imports
class Cookie:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, flavor, description, quantity):
    self.name = name
    self.flavor = flavor
    self.description = description
    self.quantity = quantity

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