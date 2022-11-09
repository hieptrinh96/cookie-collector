from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

REVIEWS = (
  ('G', 'Would recommend'),
  ('N', 'Would not recommend'),
  ('O', 'Cookie was okay'),
)

class IceCream(models.Model):
  name = models.CharField(max_length=50)
  flavor = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('iceCream_detail', kwargs={'pk': self.id})

class Cookie(models.Model):
  name = models.CharField(max_length=100)
  flavor = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  quantity = models.IntegerField()
  iceCream = models.ManyToManyField(IceCream)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('cookies_detail', kwargs={'cookie_id': self.id})

class Review(models.Model):
  date = models.DateField('Review Created on')
  review = models.CharField(
    max_length = 1,
    choices=REVIEWS,
    default=REVIEWS[0][0]
  )

  cookie = models.ForeignKey(Cookie, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_review_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

