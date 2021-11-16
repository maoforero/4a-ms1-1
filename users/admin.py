from django.contrib import admin
from .models import User,Role  #. porque importo desde la misma carpeta

# Register your models here.

admin.site.register(User)
admin.site.register(Role)