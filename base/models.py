from django.db import models

# Create your models here.
class Room(models.Model):
    # host =
    # topic =
    name = models.CharField(max_length=200)
    # participants =
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)