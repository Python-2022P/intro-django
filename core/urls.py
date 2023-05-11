from django.contrib import admin
from django.urls import path
from django.http import HttpRequest


def home(request: HttpRequest):
    print(request.method)
    print(request.path)
    print(request.content_type)
    pass

def get_params(request: HttpRequest):
    params = request.GET
    number = params.get('number')
    print(number)
    pass

def get_sum(request: HttpRequest):
    pass


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('get-num/', get_params),
    path('get-sum/', get_sum),
]
