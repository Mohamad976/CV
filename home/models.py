from django.db import models

# python manage.py makemigrations
# Create your models here.
class Home(models.Model):
    first_name = models.CharField(max_length=50)
    mid_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50)
    yourwork = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='Home/')
    telegram = models.CharField(max_length=50,blank=True)


    def __str__(self):
        return self.last_name


