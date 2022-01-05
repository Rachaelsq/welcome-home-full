from django.contrib import admin

# Register your models here.
from .models import Journal

#register models with admin panel
admin.site.register(Journal)