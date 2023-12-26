from django.db import models

# Create your models here.

# python manage.py startapp


# python manage.py runserver
# python manage.py makemigrations
# python manage.py migrate  

class Portfolio(models.Model):
    issue = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(upload_to='Portfolio/')
    time = models.DateField(auto_now=False, auto_now_add=True)



    def __str__(self):
        return self.issue
