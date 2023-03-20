from django.db import models


# Create your models
class Service(models.Model):
    name=models.CharField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='gallery',blank=True)

    def __str__(self):
        return self.name

