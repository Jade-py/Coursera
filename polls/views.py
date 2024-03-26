from django.shortcuts import render, HttpResponse

# Create your views here.
def HomeView(request):
    return HttpResponse("Hello, world. 9a047685 is the polls index.")