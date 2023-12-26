from django.db import models

# Create your models here.

# python manage.py startapp


# python manage.py runserver
# python manage.py makemigrations
# python manage.py migrate  

class About(models.Model):
    your_job = models.CharField(max_length=50,default='Mechanical engineering')
    based_in = models.CharField(max_length=50,default='Birjand - Iran')
    summery_about = models.TextField(default='salam')
    photo = models.ImageField(upload_to='About/')



    # def __str__(self):
    #     return self.last_name


class Service(models.Model):
    your_service = models.CharField(max_length=50)
    about_your_service = models.TextField()
    photo = models.ImageField(upload_to='About/service/',blank=True)

    def __str__(self):
        return self.your_service


class Skill(models.Model):
    your_skill = models.CharField(max_length=50)
    percent = models.IntegerField()

    def __str__(self):
        return self.your_skill