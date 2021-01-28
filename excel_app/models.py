from django.db import models
from django.utils.timezone import now

class File(models.Model):
    file = models.FileField()


class Contact(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField()
    create_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.name
