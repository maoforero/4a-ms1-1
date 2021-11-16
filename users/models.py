from django.db import models
from django_countries.fields import CountryField

# Create your models here.


ITEM_TYPER = (
  ('Admin','Administrador'),
  ('User', 'Usuario'),
  ('Inv','Invitado'),
)

class Role(models.Model):
    id = models.AutoField(primary_key = True)
    type = models.CharField(choices = ITEM_TYPER, max_length = 12)


ITEM_TYPE = (
    ('CC','Cédula de ciudadania'),
    ('CE','Cédula de extranjería')
)

class User(models.Model):
    
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 30,null = False)
    lastname = models.CharField(max_length = 30,null = False)
    typeid = models.CharField(choices = ITEM_TYPE, max_length = 10) #tipo de documento
    numberid = models.CharField(max_length = 12,null = False, blank = True) # numero de cedula
    phone = models.CharField(max_length = 12,null = False, blank = True)
    birth = models.DateField()   
    country = CountryField()
    city = models.CharField(max_length = 20)
    email = models.EmailField(null = False ,unique=True)
    password = models.CharField(max_length = 12)
    role = models.ForeignKey(Role, on_delete = models.CASCADE, null = False)
