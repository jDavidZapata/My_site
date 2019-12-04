from django.urls import path
from . import views

app_name = "personal"

urlpatterns = [
    #path('', views.temppage, name='temppage'),
    path('', views.personal_page, name='personal'),
]
