from django.contrib import admin
from .models import Resultado

class ResultadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'exibir_campo0', 'exibir_campo1', 'exibir_campo2', 'exibir_campo3', 'exibir_campo4']

    def exibir_campo0(self, obj):
        return obj.nome_da_receita

    def exibir_campo1(self, obj):
        return obj.valor_da_receita

    def exibir_campo2(self, obj):
        return obj.valor_da_unidade

    def exibir_campo3(self, obj):
        return obj.valor_do_lucro

    def exibir_campo4(self, obj):
        return obj.status

    exibir_campo0.short_description = 'Nome da Receita'
    exibir_campo1.short_description = 'Preço da receita'
    exibir_campo2.short_description = 'valor da unidade'
    exibir_campo3.short_description = 'Lucro'
    exibir_campo4.short_description = 'Status'

admin.site.register(Resultado, ResultadoAdmin)
