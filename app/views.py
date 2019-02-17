from django.http import HttpResponse


def index(request):
    return HttpResponse("Resume API")

def create(request):
    return HttpResponse("Create")

def edit(request):
    return HttpResponse("Edit")

def get(request):
    return HttpResponse("get")

def getAll(request):
    return HttpResponse("Get All")

def delete(request):
    return HttpResponse("Delete")