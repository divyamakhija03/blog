from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home,name='home'),
    # name is an optional hai url ki jagah ye name likh skte hai
    path('create/',views.create,name='create'),
    path('insert/',views.insert,name='insert'),
    path('edit/<pk>',views.edit,name='edit'),
    path('update/',views.update,name='update'),
    path('delete/<pk>',views.delete,name='delete'),
]