from django.contrib import admin
from django.urls import path

from .views import (
    home,
    get_params,
    get_sum,
    get_user,
    index
)


urlpatterns = [
    path('', index),
    path('home/', home),
    path('get-num/', get_params),
    path('get-sum/', get_sum),
    path('get-user/<int:username>', get_user),
]
