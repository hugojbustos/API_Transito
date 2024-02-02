from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    correo_electronico = models.EmailField()

    def __str__(self):
        return self.nombre


class Vehiculo(models.Model):
    placa_patente = models.CharField(max_length=20, unique=True)
    marca = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return self.placa_patente


class Policia(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def generar_token(self):
        token = Token.objects.get_or_create(user=self.user)
        return token.key if isinstance(token, Token) else token[0].key

    def __str__(self) -> str:
        return self.user.username


class Infraccion(models.Model):
    placa_patente = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    comentarios = models.TextField()
    oficial = models.ForeignKey(Policia, on_delete=models.CASCADE)

    def __str__(self):
        return f"Infracción {self.id} - {self.placa_patente}"
