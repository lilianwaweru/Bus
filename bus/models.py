from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length = 30)
    origin = models.CharField(max_length = 30)
    destination = models.CharField(max_length = 70)
    capacity = models.IntegerField(default=0)
    charges = models.IntegerField(default= 0)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def save_car(self):
        self.save()

class Category(models.Model):
    name = models.CharField(max_length = 30)
    cat_image = models.ImageField(upload_to = 'bus_pics/',blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length = 70)
    description = models.TextField()
    image = models.ImageField(upload_to = 'bus_pics/',blank=True)
    amount = models.CharField(max_length = 70)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    def save_image(self):
        self.save()

class Comments(models.Model):
    name = models.CharField(max_length = 30) 
    comments = models.TextField() 
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
 

