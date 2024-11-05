from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("ola mundo")

# Create your views here.
