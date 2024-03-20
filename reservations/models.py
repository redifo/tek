from django.db import models
from django.contrib.auth.models import User

class Table(models.Model):
    """model for a table in the restaurant"""
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"Table {self.table_number} at {self.location}"

class Reservation(models.Model):
    """
    model for each reservation
    """
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reserved_customer', null=True, default=None)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='reserved_tables')
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField()
    
    def __str__(self):
        return f"Reservation for {self.customer} at {self.date} {self.time}"

class SpecialRequest(models.Model):
    """
    model for a special request made on a reservation
    """
    request_text = models.TextField()
    is_approved = models.BooleanField(default=False)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='reservation_special_requests')

    def __str__(self):
        return f"{self.request_text} for ({self.reservation}) (Approved: {self.is_approved})"
