from django.shortcuts import render
from django.http import JsonResponse

def health_status(request):
    return JsonResponse({"status": "ok"})