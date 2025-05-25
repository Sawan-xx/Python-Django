from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class destinations(models.Model):
    d_name=models.CharField(max_length=50)
    d_img=models.FileField(upload_to='destination')
    discription=models.TextField()
    price=models.IntegerField()

    def __str__(self):
        return f'{self.d_img} {self.d_name} {self.discription} {self.price}'
    

class booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=100)
    booking_date = models.DateTimeField(auto_now=True)
    travel_date = models.DateField()
    contact=models.IntegerField(null=True)

    def __str__(self):
        return f'{self.user} {self.destination} {self.booking_date} {self.travel_date}'
    
class cars (models.Model):
    car_name=models.CharField(max_length=50)
    car_colour=models.CharField(max_length=50)
    car_img=models.FileField(upload_to='cars')
    description=models.TextField()

    def __str__(self):
        return f'{self.car_name} { self.car_img } {self.car_colour} { self.description }'
    
class Contact(models.Model):
    Name=models.CharField(max_length=100)
    Contact=models.CharField(max_length=13)
    Email=models.EmailField(null=False)
    def __str__(self):
        return f'{self.Name} { self.Contact } {self.Email}'