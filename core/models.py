from django.db import models

# Create your models here.

class Some(models.Model):
    test = models.CharField(max_length=300)
    element = models.FileField(upload_to='test', max_length=255)
