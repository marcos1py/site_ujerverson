from django.db import models

class Resultado(models.Model):
    id = models.AutoField(primary_key=True)
    nome_da_receita = models.CharField(max_length=255)
    valor_da_receita = models.FloatField()
    valor_da_unidade = models.FloatField()
    valor_do_lucro = models.FloatField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Resultado {self.pk}"