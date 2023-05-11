from django.contrib import admin
from django.urls import path


def home(request):
    print(request.method)
    pass


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
]
