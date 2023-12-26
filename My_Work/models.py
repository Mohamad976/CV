from django.db import models

# Create your models here.

# python manage.py startapp


# python manage.py runserver
# python manage.py makemigrations
# python manage.py migrate  

class MY_WORK(models.Model):
    issue = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(upload_to='My_Work/')

    def __str__(self):
        return self.issue
