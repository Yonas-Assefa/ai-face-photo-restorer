from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.


def frontPage(request):
    return render(request,'core/frontpage.html')

def signup(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)

        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('frontpage')
        
    context={'form':form}
    return render(request,'core/signup.html',context)