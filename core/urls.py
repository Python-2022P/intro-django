from django.contrib import admin
from django.urls import path
from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Hello</h1>')

def get_params(request: HttpRequest):
    params = request.GET
    number = params.get('number')
    print(number)
    pass

def get_sum(request: HttpRequest):
    params = request.GET

    a = params.get('a', 0)
    b = params.get('b', 0)

    result = {
        'result': int(a) + int(b)
    }
    print(result)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('get-num/', get_params),
    path('get-sum/', get_sum),
]
