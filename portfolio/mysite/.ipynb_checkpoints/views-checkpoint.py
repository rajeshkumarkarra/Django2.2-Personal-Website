# views.py is responsiable to display the stuff on web browser

"""
# Create your views here.
# HttpResponse is responsiable for displaying the stuff on web browser
from django.http import HttpResponse
def index(request):
    return HttpResponse("hello rajesh! welcome to the tech world")
"""
# request is basically user sends a request to server
# render is working on index.html file and hide waste stuff and render some results to user
from django.shortcuts import render
def index(request):
    return render(request, 'mysite/index.html')

def portfolio(request):
    return render(request, 'mysite/portfolio.html')

def contact(request):
    return render(request, 'mysite/contact.html')