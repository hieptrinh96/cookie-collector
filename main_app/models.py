from django.db import models
from django.urls import reverse
# Create your models here.
class Cookie(models.Model):
  name = models.CharField(max_length=100)
  flavor = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  quantity = models.IntegerField()

  def __str__(self):
    return self.name