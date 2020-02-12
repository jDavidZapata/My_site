from django.urls import path, include
from users import views as user_views

app_name = 'users'

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', user_views.login_, name='login'),
    path('profile/', user_views.profile, name='profile'),
    path('logout/', user_views.logout_, name='logout'),
    
] 