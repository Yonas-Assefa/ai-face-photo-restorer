from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Notificaion


# Create your views here.
@login_required 
def notifications(request):
    goto=request.GET.get('goto','')
    notification_id=request.GET.get('notification',0)
    extra_id=request.GET.get('extra_id',0)
    
    if goto !='':
        notification=Notificaion.objects.get(pk=notification_id)
        notification.is_read=True
        notification.save()

        if notification.notification_type == Notificaion.MESSAGE:
            return redirect('view_application',application_id=notification.extra_id)

        elif notification.notification_type==Notificaion.APPLICATION:
            return redirect('view_application',application_id=notification.extra_id)
    return render(request,'notification/notifications.html')