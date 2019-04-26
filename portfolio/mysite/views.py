# views.py is responsiable to display the stuff on web browser
from django.shortcuts import render

# Create your views here.
# HttpResponse is responsiable for displaying the stuff on web browser
from django.http import HttpResponse
def index(request):
    return HttpResponse("hello rajesh! welcome to the tech world")
