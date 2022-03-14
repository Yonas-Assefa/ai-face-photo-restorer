from django.shortcuts import render

# Create your views here.


def frontPage(request):
    return render(request,'core/frontpage.html')

def signup(request):
    return render(request,'core/signup.html')