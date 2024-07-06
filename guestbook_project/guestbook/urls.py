from django.urls import path
from . import views

urlpatterns = [
    path('', views.guestbook_home, name='guestbook_home'),
    path('add/', views.add_guestbook_entry, name='add_guestbook_entry'),
]
