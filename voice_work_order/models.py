from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)

class Plane(models.Model):
    model = models.CharField(max_length=50)

class PlanePart(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    plane = models.ForeignKey('Plane')

class WorkOrder(models.Model):
    ordertype = models.CharField(max_length=50)
    textbox = models.CharField(max_length=50)
    textarea = models.TextField()
    CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    )
    select = models.CharField(max_length=1,choices=CHOICES,default='A')
    radio = models.CharField(max_length=1,choices=CHOICES,default='A')
    checkbox = models.CharField(max_length=50)
    session = models.ForeignKey('Session')

class Session(models.Model):
    customer = models.OneToOneField('Customer')
    plane = models.OneToOneField('Plane')
