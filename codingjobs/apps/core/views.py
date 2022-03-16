from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from apps.job.models import Job
from apps.userprofile.models import Userprofile
# Create your views here.


def frontPage(request):
    jobs=Job.objects.filter(status=Job.ACTIVE).order_by('-created_at')[0:3]
    context={'jobs':jobs}
    return render(request,'core/frontpage.html',context)

def signup(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)

        if form.is_valid():
            user=form.save()

            account_type=request.POST.get('account_type','jobseeker')
            if account_type=="employer":
                userprofile=Userprofile.objects.create(user=user,is_employer=True)
                userprofile.save()
            else:
                userprofile=Userprofile.objects.create(user=user)
                userprofile.save()
                
            login(request,user)
            return redirect('dashboard')
        
    context={'form':form}
    return render(request,'core/signup.html',context)