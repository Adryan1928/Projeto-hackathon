from django.db import models


class Campo(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.CharField(max_length=255)

class Promocao(models.Model):
    desconto = models.FloatField()
    data_final = models.DateField()
    data_inicial = models.DateField()


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.FloatField()
    campo = models.ManyToManyField(Campo, )
    modelo = models.CharField(max_length=255)    
    promocao = models.ForeignKey(Promocao, on_delete=models.CASCADE, null=True)
    id_empresa = models.IntegerField()





