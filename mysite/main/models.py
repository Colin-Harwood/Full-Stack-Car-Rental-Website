from django.db import models

class BookingDetails(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    pickUp = models.CharField(max_length=200)
    dropOff = models.CharField(max_length=200)
    vehicle = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
