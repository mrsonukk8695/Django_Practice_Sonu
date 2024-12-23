from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("Hello this is Home page of Chai aur code...")
    return render(request, 'website/index.html')


def about(request):
    return HttpResponse("Hello this is About page of Chai aur code...")


def contact(request):
    return HttpResponse("Hello this is Contacts page of Chai aur code...")