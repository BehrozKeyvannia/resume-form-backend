from django.http import JsonResponse, HttpResponse, HttpResponseForbidden
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from random import randint
from os import listdir
from os.path import isfile, join
import os
from pathlib import Path

import pprint
import pdb
import json

def index(request):
    return HttpResponse("Resume API")

@csrf_exempt
def create(request):
    data = extractJsonData(request.body)
    if request.method == 'POST':
        if data:
            id = generateId()
            writeToFile(id, data)
            return JsonResponse({
                "id": id
            })
        else:
            return HttpResponse(status=500)
    elif request.method == 'GET':
        return HttpResponseForbidden()

@csrf_exempt
def edit(request, id):
    if request.method == 'POST':
        data = extractJsonData(request.body)
        writeToFile(id, data)
        return JsonResponse({
            "data": "saved"
        })
    elif request.method == 'GET':
        return HttpResponseForbidden()

def get(request, id):
    if request.method == 'POST':
        return HttpResponseForbidden()
    elif request.method == 'GET':
        return JsonResponse({
            "method": "get"
        })

def getAll(request):
    if request.method == 'GET':
        path = "./files"
        Path(path).mkdir(parents=True, exist_ok=True)
        allFiles = [f for f in listdir(path) if isfile(join(path, f))]
        jsonData = []
        for file in allFiles:
            id = file.strip(".json")
            if readFromFile(id):
                fileData = readFromFile(id)
                fileData['id'] = id
                jsonData.append(fileData)
        return JsonResponse({
            "data": jsonData
        })
    elif request.method == 'POST':
        return HttpResponseForbidden()

@csrf_exempt
def delete(request, id):
    if request.method == 'DELETE':
        deleteFile(id)
        return JsonResponse({
            "data": "deleted"
        })
    elif request.method == 'GET':
        return HttpResponseForbidden()

def extractJsonData(value):
    body_unicode = value.decode('utf-8')
    body = json.loads(body_unicode)
    return body

def writeToFile(id, data):
    path = "./files/{}.json".format(id)
    file = open(path,'w')
    # parsedData = json.dumps(str(data).replace("\'", "\""), indent=4)
    parsedData = json.dumps(data, indent=4)
    file.write(str(parsedData))
    file.close()


def readFromFile(id):
    try:
        file = open("./files/{}.json".format(id),'r')
        data = file.read()
        parsedData = json.loads(str(data))
        file.close()
        return parsedData
    except:
        return False

def deleteFile(id):
    try:
        os.remove("./files/{}.json".format(id));
    except Exception as e:
        print("deleteFileError: " + str(e));

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def generateId():
    return random_with_N_digits(5)