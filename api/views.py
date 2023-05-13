from django.http import HttpRequest, HttpResponse, JsonResponse
import json

def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Hello</h1>')

def get_params(request: HttpRequest):
    params = request.GET
    number = params.get('number')
    print(number)
    pass

def get_sum(request: HttpRequest):
    if request.method == 'GET':
        params = request.GET

        a = params.get('a', 0)
        b = params.get('b', 0)

        result = {
            'result': int(a) + int(b)
        }
        
        return JsonResponse(result)
    
    elif request.method == "POST":
        body = request.body.decode()

        data = json.loads(body)

        print(data)
        print(type(data))

        return JsonResponse({'result': data['a'] + data['b']})
    

def get_user(request: HttpRequest, username: str) -> JsonResponse:
    return JsonResponse({'username': username})