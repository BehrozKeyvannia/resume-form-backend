from django.http import JsonResponse, HttpResponse, HttpResponseForbidden
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
import pdb

def index(request):
    return HttpResponse("Resume API")

@csrf_exempt
def create(request):
    pdb.set_trace()
    if request.method == 'POST':
        return JsonResponse({
            "method": "post"
        })
    elif request.method == 'GET':
        return HttpResponseForbidden()

@csrf_exempt
def edit(request):
    if request.method == 'POST':
        return JsonResponse({
            "method": "post"
        })
    elif request.method == 'GET':
        return HttpResponseForbidden()

def get(request):
    return HttpResponse("get")

def getAll(request):
    return HttpResponse("Get All")

def delete(request):
    return HttpResponse("Delete")