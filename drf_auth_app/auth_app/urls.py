from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('sign-up', views.signup),
    path('sign-in', views.signin),
    path('users', views.user_list)
]