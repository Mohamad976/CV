from django.contrib import admin

# Register your models here.
from .models import About
from .models import Service
from .models import Skill


admin.site.register(About)
admin.site.register(Service)
admin.site.register(Skill)