from django.contrib import admin
from django.urls import path
from api.views import (
    home,
    get_params,
    get_sum
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('get-num/', get_params),
    path('get-sum/', get_sum),
]
