from django.contrib import admin

# Register your models here.
from .models import Cryptocurrency

admin.site.register(Cryptocurrency)