from django.shortcuts import render, get_object_or_404
from contas.contas import calcular_receita_cafe, calcular_receita_coco, calcular_receita_leite_po
from .models import Resultado

def home(request):
    if request.method == 'POST':
        if request.POST.get('acao') == 'Calcular':
            quantidadeChocolate = float(request.POST.get('quantidade-Chocolate'))
            quantidadeManteiga = float(request.POST.get('quantidade-Manteiga'))
            quantidadeLeiteCondensado = float(request.POST.get('quantidade-Leite-condensado'))
            quantidadeLeiteEmPo = float(request.POST.get('quantidade-Leite-em-po'))
            quantidadeCafe = float(request.POST.get('quantidade-cafe'))
            quantidadeCoco = float(request.POST.get('quantidade-coco'))

            valorChocolate = float(request.POST.get('valor-Chocolate'))
            valorManteiga = float(request.POST.get('valor-Manteiga'))
            valorLeiteCondensado = float(request.POST.get('valor-Leite-condensado'))
            valorLeiteEmPo = float(request.POST.get('valor-Leite-em-po'))
            valorCafe = float(request.POST.get('valor-cafe'))
            valorCoco = float(request.POST.get('valor-coco'))

            aumentarReceita = 1
            valorUnitarioU = 2.0

            valor_da_receita1, valor_da_unidade1, valor_do_lucro1, status_ninho1 = calcular_receita_leite_po(quantidadeChocolate, quantidadeLeiteCondensado, quantidadeManteiga, quantidadeLeiteEmPo, valorChocolate, valorLeiteCondensado, valorManteiga, valorLeiteEmPo, aumentarReceita, valorUnitarioU)
            valor_da_receita2, valor_da_unidade2, valor_do_lucro2, status_cafe1 = calcular_receita_cafe(quantidadeChocolate, quantidadeLeiteCondensado, quantidadeManteiga, quantidadeCafe, valorChocolate, valorLeiteCondensado, valorManteiga, valorCafe, aumentarReceita, valorUnitarioU)
            valor_da_receita3, valor_da_unidade3, valor_do_lucro3, status_coco1 = calcular_receita_coco(quantidadeChocolate, quantidadeLeiteCondensado, quantidadeManteiga, quantidadeCoco, valorChocolate, valorLeiteCondensado, valorManteiga, valorCoco, aumentarReceita, valorUnitarioU)


            resultado1 = Resultado(id = 1 ,nome_da_receita="receita_coco",valor_da_receita=valor_da_receita1,
                                    valor_da_unidade=valor_da_unidade1,
                                    valor_do_lucro=valor_do_lucro1,
                                    status=status_ninho1)
            resultado1.save()

            resultado2 = Resultado(id = 2 ,nome_da_receita="receita_cafe",valor_da_receita=valor_da_receita2,
                                    valor_da_unidade=valor_da_unidade2,
                                    valor_do_lucro=valor_do_lucro2,
                                    status=status_cafe1)
            resultado2.save()

            resultado3 = Resultado(id = 3 ,nome_da_receita="receita_coco",valor_da_receita=valor_da_receita3,
                                    valor_da_unidade=valor_da_unidade3,
                                    valor_do_lucro=valor_do_lucro3,
                                    status=status_coco1)
            if not status_ninho1:
                status_ninho1 = "imgFALSE"
            else:
                status_ninho1 = "imgOK"

            if not status_cafe1:
                status_cafe1 = "imgFALSE"
            else:
                status_cafe1 = "imgOK"

            if not status_coco1:
                status_coco1 = "imgFALSE"
            else:
                status_coco1 = "imgOK"

            context = {
                'valor_de_venda1':2,
                'valor_de_venda2':2,
                'valor_de_venda3':2,

                'quantidade_receita1':1,
                'quantidade_receita2':1,
                'quantidade_receita3':1,

                'valor_da_receita1': f"{valor_da_receita1:.2f}",
                'valor_da_unidade1': valor_da_unidade1,
                'valor_do_lucro1': f"{valor_do_lucro1:.2f}",
                'status_ninho1': status_ninho1,

                'valor_da_receita2': f"{valor_da_receita2:.2f}",
                'valor_da_unidade2': valor_da_unidade2,
                'valor_do_lucro2': f"{valor_do_lucro2:.2f}",
                'status_cafe1': status_cafe1,

                'valor_da_receita3': f"{valor_da_receita3:.2f}",
                'valor_da_unidade3': valor_da_unidade3,
                'valor_do_lucro3': f"{valor_do_lucro3:.2f}",
                'status_coco1': status_coco1,
            }
            return render(request, "ingredientes/resultados.html", context=context)

    return render(request, "ingredientes/home.html", context={})

def resultados(request):
    if request.method == 'POST':
        if request.POST.get('acao') == 'atualizar':
            receita_leite_ninho = Resultado.objects.get(id=1)
            valor_da_receita1 = receita_leite_ninho.valor_da_receita
            valor_do_lucro1 = receita_leite_ninho.valor_do_lucro
            status_ninho1 = receita_leite_ninho.status
            valor_da_unidade1 = receita_leite_ninho.valor_da_unidade

            receita_cafe = Resultado.objects.get(id=2)
            valor_da_receita2 = receita_cafe.valor_da_receita
            valor_do_lucro2 = receita_cafe.valor_do_lucro
            status_cafe1 = receita_cafe.status
            valor_da_unidade2 = receita_cafe.valor_da_unidade     
            
            receita_coco = Resultado.objects.get(id=3)
            valor_da_receita3 = receita_coco.valor_da_receita
            valor_do_lucro3 = receita_coco.valor_do_lucro
            status_coco1 = receita_coco.status
            valor_da_unidade3 = receita_coco.valor_da_unidade

            
            quantidade_do_user_leite_ninho = float(request.POST.get('quantidade1'))
            preço_do_user_leite_ninho = float(request.POST.get('valor1'))
            #receita atualizada
            valor_da_receita1 =  valor_da_receita1  * quantidade_do_user_leite_ninho
            #calcula valor do lucro
            valor_do_lucro1 = preço_do_user_leite_ninho * (50 * quantidade_do_user_leite_ninho) - valor_da_receita1

            quantidade_do_user_coco = float(request.POST.get('quantidade2'))
            preço_do_user_coco = float(request.POST.get('valor2'))
            valor_da_receita2 =  valor_da_receita2  * quantidade_do_user_coco
            valor_do_lucro2 = preço_do_user_coco * (50 * quantidade_do_user_coco) - valor_da_receita2


            quantidade_do_user_cafe = float(request.POST.get('quantidade3'))
            preço_do_user_cafe = float(request.POST.get('valor3'))
            valor_da_receita3 =  valor_da_receita3  * quantidade_do_user_cafe
            valor_do_lucro3 = preço_do_user_cafe * (50 * quantidade_do_user_cafe) - valor_da_receita3


            if valor_da_receita1 >= 60:
                status_ninho1 = "imgFALSE"
            else:
                status_ninho1 = "imgOK"

            if valor_da_receita2 >= 60:
                status_cafe1 = "imgFALSE"
            else:
                status_cafe1 = "imgOK"

            if  valor_da_receita3 >= 60:

                status_coco1 = "imgFALSE"
            else:
                status_coco1 = "imgOK"

            context = {
                'valor_de_venda1':preço_do_user_leite_ninho,
                'valor_de_venda2':preço_do_user_coco,
                'valor_de_venda3':preço_do_user_cafe,

                'quantidade_receita1':quantidade_do_user_leite_ninho,
                'quantidade_receita2':quantidade_do_user_coco,
                'quantidade_receita3':quantidade_do_user_cafe,

                'valor_da_receita1': f"{valor_da_receita1:.2f}",
                'valor_da_unidade1': valor_da_unidade1,
                'valor_do_lucro1': f"{valor_do_lucro1:.2f}",
                'status_ninho1': status_ninho1,

                'valor_da_receita2': f"{valor_da_receita2:.2f}",
                'valor_da_unidade2': valor_da_unidade2,
                'valor_do_lucro2': f"{valor_do_lucro2:.2f}",
                'status_cafe1': status_cafe1,

                'valor_da_receita3': f"{valor_da_receita3:.2f}",
                'valor_da_unidade3': valor_da_unidade3,
                'valor_do_lucro3': f"{valor_do_lucro3:.2f}",
                'status_coco1': status_coco1,
            }
            return render(request, "ingredientes/resultados.html", context=context)

        else:
            quantidadeChocolate = float(request.POST.get('quantidade-Chocolate'))
            quantidadeManteiga = float(request.POST.get('quantidade-Manteiga'))
            quantidadeLeiteCondensado = float(request.POST.get('quantidade-Leite-condensado'))
            quantidadeLeiteEmPo = float(request.POST.get('quantidade-Leite-em-po'))
            quantidadeCafe = float(request.POST.get('quantidade-cafe'))
            quantidadeCoco = float(request.POST.get('quantidade-coco'))

            valorChocolate = float(request.POST.get('valor-Chocolate'))
            valorManteiga = float(request.POST.get('valor-Manteiga'))
            valorLeiteCondensado = float(request.POST.get('valor-Leite-condensado'))
            valorLeiteEmPo = float(request.POST.get('valor-Leite-em-po'))
            valorCafe = float(request.POST.get('valor-cafe'))
            valorCoco = float(request.POST.get('valor-coco'))

            aumentarReceita = 1
            valorUnitarioU = 2.0

            valor_da_receita1, valor_da_unidade1, valor_do_lucro1, status_ninho1 = calcular_receita_leite_po(quantidadeChocolate, quantidadeLeiteCondensado, quantidadeManteiga, quantidadeLeiteEmPo, valorChocolate, valorLeiteCondensado, valorManteiga, valorLeiteEmPo, aumentarReceita, valorUnitarioU)
            valor_da_receita2, valor_da_unidade2, valor_do_lucro2, status_cafe1 = calcular_receita_cafe(quantidadeChocolate, quantidadeLeiteCondensado, quantidadeManteiga, quantidadeCafe, valorChocolate, valorLeiteCondensado, valorManteiga, valorCafe, aumentarReceita, valorUnitarioU)
            valor_da_receita3, valor_da_unidade3, valor_do_lucro3, status_coco1 = calcular_receita_coco(quantidadeChocolate, quantidadeLeiteCondensado, quantidadeManteiga, quantidadeCoco, valorChocolate, valorLeiteCondensado, valorManteiga, valorCoco, aumentarReceita, valorUnitarioU)

            resultado1 = Resultado(id = 1 ,nome_da_receita="receita_coco",valor_da_receita=valor_da_receita1,
                                    valor_da_unidade=valor_da_unidade1,
                                    valor_do_lucro=valor_do_lucro1,
                                    status=status_ninho1)
            resultado1.save()

            resultado2 = Resultado(id = 2 ,nome_da_receita="receita_cafe",valor_da_receita=valor_da_receita2,
                                    valor_da_unidade=valor_da_unidade2,
                                    valor_do_lucro=valor_do_lucro2,
                                    status=status_cafe1)
            resultado2.save()

            resultado3 = Resultado(id = 3 ,nome_da_receita="receita_coco",valor_da_receita=valor_da_receita3,
                                    valor_da_unidade=valor_da_unidade3,
                                    valor_do_lucro=valor_do_lucro3,
                                    status=status_coco1)

            resultado3.save()
            print(status_ninho1)
            if status_ninho1 == False:
                status_ninho1 = "imgFALSE"
            else:
                status_ninho1 = "imgOK"

            if status_cafe1 == False:
                status_cafe1 = "imgFALSE"
            else:
                status_cafe1 = "imgOK"

            if  status_coco1 == False:

                status_coco1 = "imgFALSE"
            else:
                status_coco1 = "imgOK"

            context = {
                'valor_de_venda1':2,
                'valor_de_venda2':2,
                'valor_de_venda3':2,

                'quantidade_receita1':1,
                'quantidade_receita2':1,
                'quantidade_receita3':1,

                'valor_da_receita1': f"{valor_da_receita1:.2f}",
                'valor_da_unidade1': valor_da_unidade1,
                'valor_do_lucro1': f"{valor_do_lucro1:.2f}",
                'status_ninho1': status_ninho1,

                'valor_da_receita2': f"{valor_da_receita2:.2f}",
                'valor_da_unidade2': valor_da_unidade2,
                'valor_do_lucro2': f"{valor_do_lucro2:.2f}",
                'status_cafe1': status_cafe1,

                'valor_da_receita3': f"{valor_da_receita3:.2f}",
                'valor_da_unidade3': valor_da_unidade3,
                'valor_do_lucro3': f"{valor_do_lucro3:.2f}",
                'status_coco1': status_coco1,
            }
            return render(request, "ingredientes/resultados.html", context=context)

    return render(request, "ingredientes/resultados.html", context={})
