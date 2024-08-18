from django.urls import path
from . import views
urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/D/<slug:slug>', views.details,name='details'),
    path('', views.main, name='main'),
    path('testing/<int:num>', views.testing, name='testing'),
]