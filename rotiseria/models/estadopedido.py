from django.db import models

class EstadoPedido (models.Model):
    estado= models.CharField(max_length=40)  #  pendiente  cancelado  confirmado  entregado en local

    def __str__(self):
        return str(self.estado)