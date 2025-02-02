from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Car model
class Car(models.Model):
    car_name = models.CharField(max_length=30)
    car_desc = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="media/makinat", default="media/makinat/default.jpg")

    def __str__(self):
        return self.car_name


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    availability = models.BooleanField(default=True)
    vehicle_assigned = models.ForeignKey(Car, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Task(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserDriver(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)


# Order model
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    cars = models.ManyToManyField(Car)  # Many-to-many relationship with Car
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True,
                               blank=True)  # Optional ForeignKey to Driver
    days_for_rent = models.IntegerField(default=0)
    date = models.DateField(default=now)
    loc_from = models.CharField(max_length=50)
    loc_to = models.CharField(max_length=50)

    def __str__(self):
        return f"Order by {self.name} on {self.date}"


# Contact model
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, default="")
    email = models.EmailField(max_length=150, default="")
    phone_number = models.CharField(max_length=15, default="")
    message = models.TextField(max_length=500, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
