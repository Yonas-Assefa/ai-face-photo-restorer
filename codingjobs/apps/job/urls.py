from django.urls import path,include
from .views import job_detail,add_job

urlpatterns=[
    path('add/',add_job,name='add_job'),
    path('<int:job_id>/',job_detail,name='add_job')
]