from django.http import JsonResponse

def custom_404(request, exception):
    return JsonResponse(
        {"error": "The resource you are looking for was not found."},
        status=404
    )