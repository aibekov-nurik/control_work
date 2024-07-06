from django.urls import path
from . import views

urlpatterns = [
    path('', views.guestbook_home, name='guestbook_home'),
    path('add/', views.add_guestbook_entry, name='add_guestbook_entry'),
    path('edit/<int:pk>/', views.edit_guestbook_entry, name='edit_guestbook_entry'),
    path('delete/<int:pk>/', views.delete_guestbook_entry, name='delete_guestbook_entry'),
]
