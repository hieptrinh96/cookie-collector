from django.urls import path
from .import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cookies/', views.cookies_index, name='cookies_index'),
  path('cookies/<int:cookie_id>/', views.cookies_detail, name='cookies_detail'),
  path('cookies/create/', views.CookieCreate.as_view(), name='cookies_create'),
  path('cookies/<int:pk>/update/', views.CookieUpdate.as_view(), name='cookies_update'),
  path('cookies/<int:pk>/delete/', views.CookieDelete.as_view(), name='cookies_delete'),
  path('cookies/<int:cookie_id>/add_review/', views.add_review, name='add_review'),
]