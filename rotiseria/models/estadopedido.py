from django.db import models

class Estadopedido (models.Model):
    estado= models.IntegerField()  # 1 pendiente   2cancelado   3confirmado   4entregado

    def __str__(self):
        return str(self.estado)