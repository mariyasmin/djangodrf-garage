from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Veiculo(models.Model):
    motorista = models.CharField(max_length=255)
    placa = models.CharField(max_length=32)
    preco = models.DecimalField(max_digits=20, decimal_places=2)
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, related_name="veiculo")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="veiculo")

    def __str__(self):
        return f'{self.motorista} ({self.placa})'
