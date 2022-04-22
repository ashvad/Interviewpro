from django.db import models


class Address(models.Model):
    Name = models.CharField(max_length=120)
    Date = models.DateField()
    Email = models.EmailField(max_length=120)
    income = models.PositiveIntegerField()
    Ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.Name

