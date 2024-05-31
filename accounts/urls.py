from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('', include('dj_rest_auth.registration.urls')),
    path('username/', user_name)
] 