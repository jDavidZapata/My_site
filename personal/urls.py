from django.urls import path
from . import views

app_name = "personal"

urlpatterns = [
    path('personal/', views.temppage, name='temppage'),
]
