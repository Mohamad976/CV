from django.contrib import admin

# Register your models here.
from .models import Portfolio,Work

admin.site.register(Portfolio)
admin.site.register(Work)
