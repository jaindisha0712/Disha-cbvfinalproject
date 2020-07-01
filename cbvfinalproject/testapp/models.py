from django.db import models
from django.urls import reverse
# Create your models here.
class Beer(models.Model):
    name=models.CharField(max_length=256)
    colour=models.CharField(max_length=256)
    taste=models.CharField(max_length=256)
    price=models.IntegerField()

    def __str__(self):
        
        return self.name

    def get_absolute_url(self):

        return reverse('detail',kwargs={'pk':self.pk})
