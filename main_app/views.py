from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

# Add the Cat class & list and view function below the imports
class Cookie:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, flavor, description, quantity):
    self.name = name
    self.flavor = flavor
    self.description = description
    self.quantity = quantity
    

cookies = [
  Cookie('Milk Chocolate Chip', 'Milk Chocolate Chip', 'the classic- thinkc,soft, and packed with milk chocolate chips', 3),
  Cookie('Peanut Butter', 'Peanut Butter', 'A blast of flavors including peanut butter, nougat, vanilla bean, and milk chocolate', 2),
  Cookie('Blue Monster', 'brown sugar and chips ahoy', 'a cookie popping with brown sugar, semi-sweet chocolate chips, and chips ahoy', 4),
  Cookie('Almond Coconut', 'coconut and fudge', 'a rich chocolatey cookie topped with a spread of sweet coconut, melty milk chocolate, and crunchy almonds', 6)
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cookies_index(request):
  return render(request, 'cookies/index.html', {'cookies': cookies})