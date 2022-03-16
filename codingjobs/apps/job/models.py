from pyexpat import model
from tkinter import CASCADE
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model):
    SIZE_1_9='size_1_9'
    SIZE_10_49='size_10_49'
    SIZE_50_99='size_50_99'
    SIZE_100='size_100'

    CHOICES_SIZE=(
        (SIZE_1_9,'1_9'),
        (SIZE_10_49,'10_49'),
        (SIZE_50_99,'50_99'),
        (SIZE_100,'100+')
    )

    title=models.CharField(max_length=250)
    short_description=models.TextField()
    long_description=models.TextField(blank=True,null=True)

    company_name=models.CharField(max_length=225)
    company_address=models.CharField(max_length=225,blank=True,null=True)
    company_zipcode=models.CharField(max_length=225,blank=True,null=True)
    company_place=models.CharField(max_length=225,blank=True,null=True)
    company_country=models.CharField(max_length=225,blank=True,null=True)
    company_size=models.CharField(max_length=20,choices=CHOICES_SIZE,default=SIZE_1_9)

    created_by=models.ForeignKey(User,related_name='jobs',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    changed_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    job=models.ForeignKey(Job,related_name='applications',on_delete=models.CASCADE)
    content=models.TextField()
    experiance=models.TextField()

    created_by=models.ForeignKey(User,related_name='applications',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)