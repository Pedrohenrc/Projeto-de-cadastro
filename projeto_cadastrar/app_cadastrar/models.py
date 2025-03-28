from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    numcard = models.CharField(max_length=16)
    titcard = models.CharField(max_length=255)
    expiry_date = models.CharField(max_length=7)
    securycard = models.CharField(max_length=4)