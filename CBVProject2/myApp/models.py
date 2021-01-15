from django.db import models
from django.urls import reverse
# Create your models here.
class HOD(models.Model):
    name = models.CharField(max_length = 50)
    no = models.IntegerField()
    exp = models.IntegerField()
    sal = models.IntegerField()
    dept = models.CharField(max_length = 40)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
