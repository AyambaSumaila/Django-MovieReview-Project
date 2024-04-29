from django.contrib import admin # type: ignore

# Register your models here.

from .models import News 

admin.site.register(News)
