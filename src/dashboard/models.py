from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Employee(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=64)
    salary = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    grad = models.CharField(max_length=64)
    children = models.PositiveIntegerField(default=0)
    is_marie = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)