from django.db import models

class Humanos(models.Model):
    FecReg = models.DateTimeField(auto_now_add=True)
    Nombres = models.CharField(max_length=50)
    ApeUno = models.CharField(max_length=20)
    ApeDos = models.CharField(max_length=20)
    ApeTres = models.CharField(max_length=20)
