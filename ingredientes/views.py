from django.shortcuts import render
from contas.contas import calcular_receita_leite_po, calcular_receita_cafe, calcular_receita_coco

def home(request):
    if request.method == 'POST':
        quantidadeChocolate = float(request.POST.get('quantidade-Chocolate', 0.0))
        quantidadeManteiga = float(request.POST.get('quantidade-Manteiga', 0.0))
        quantidadeLeiteCondensado = float(request.POST.get('quantidade-Leite-condensado', 0.0))
        quantidadeLeiteEmPo = float(request.POST.get('quantidade-Leite-em-po', 0.0))
        quantidadeCafe = float(request.POST.get('quantidade-cafe', 0.0))
        quantidadeCoco = float(request.POST.get('quantidade-coco', 0.0))

        valorChocolate = float(request.POST.get('valor-Chocolate', 0.0))
        valorManteiga = float(request.POST.get('valor-Manteiga', 0.0))
        valorLeiteCondensado = float(request.POST.get('valor-Leite-condensado', 0.0))
        valorLeiteEmPo = float(request.POST.get('valor-Leite-em-po', 0.0))
        valorCafe = float(request.POST.get('valor-cafe', 0.0))
        valorCoco = float(request.POST.get('valor-coco', 0.0))

        
        aumentarReceita = 1
        valorUnitarioU = 2.0

        aumentarReceita = 1
        valorUnitarioU = 2.0

        valor_da_receita1 ,valor_da_unidade1,valor_do_lucro1, status_ninho1 = calcular_receita_leite_po(quantidadeChocolate, quantidadeLeiteCondensado, quantidadeManteiga, quantidadeLeiteEmPo, valorChocolate, valorLeiteCondensado,valorManteiga, valorLeiteEmPo, aumentarReceita, valorUnitarioU)
        valor_da_receita2 ,valor_da_unidade2,valor_do_lucro2, status_cafe1 = calcular_receita_cafe(quantidadeChocolate, quantidadeLeiteCondensado, quantidadeManteiga, quantidadeCafe, valorChocolate, valorLeiteCondensado,valorManteiga, valorCafe, aumentarReceita, valorUnitarioU)
        valor_da_receita3 ,valor_da_unidade3,valor_do_lucro3, status_coco1 = calcular_receita_coco(quantidadeChocolate, quantidadeLeiteCondensado, quantidadeManteiga, quantidadeCoco, valorChocolate, valorLeiteCondensado,valorManteiga, valorCoco, aumentarReceita, valorUnitarioU)

        
        if status_ninho1 == False:
            status_ninho1 = "imgFALSE"
        else:
            status_ninho1 = "imgOK"

        if status_cafe1 == False:
            status_cafe1 = "imgFALSE"
        else:
            status_cafe1 = "imgOK"

        if status_coco1 == False:
            status_coco1 = "imgFALSE"
        else:
            status_coco1 = "imgOK"

        context = {
            'valor_da_receita1': f"{valor_da_receita1:.2f}",
            'valor_da_unidade1': valor_da_unidade1,
            'valor_do_lucro1': valor_do_lucro1,
            'status_ninho1': status_ninho1,

            'valor_da_receita2': f"{valor_da_receita2:.2f}",
            'valor_da_unidade2': valor_da_unidade2,
            'valor_do_lucro2': valor_do_lucro2,
            'status_cafe1': status_cafe1,
            
            'valor_da_receita3': f"{valor_da_receita3:.2f}",
            'valor_da_unidade3': valor_da_unidade3,
            'valor_do_lucro3': valor_do_lucro3,
            'status_coco1': status_coco1,   
        }
        return render(request, "ingredientes/resultados.html", context=context)
    
    return render(request, "ingredientes/home.html", context={})

    

def resultados(request):
    if request.method == 'POST' :

        quantidadeChocolate = float(request.POST.get('quantidade-Chocolate', 0.0))
        quantidadeManteiga = float(request.POST.get('quantidade-Manteiga', 0.0))
        quantidadeLeiteCondensado = float(request.POST.get('quantidade-Leite-condensado', 0.0))
        quantidadeLeiteEmPo = float(request.POST.get('quantidade-Leite-em-po', 0.0))
        quantidadeCafe = float(request.POST.get('quantidade-cafe', 0.0))
        quantidadeCoco = float(request.POST.get('quantidade-coco', 0.0))

        valorChocolate = float(request.POST.get('valor-Chocolate', 0.0))
        valorManteiga = float(request.POST.get('valor-Manteiga', 0.0))
        valorLeiteCondensado = float(request.POST.get('valor-Leite-condensado', 0.0))
        valorLeiteEmPo = float(request.POST.get('valor-Leite-em-po', 0.0))
        valorCafe = float(request.POST.get('valor-cafe', 0.0))
        valorCoco = float(request.POST.get('valor-coco', 0.0))

        
        aumentarReceita = 1
        valorUnitarioU = 2.0

        aumentarReceita = 1
        valorUnitarioU = 2.0

        valor_da_receita1 ,valor_da_unidade1,valor_do_lucro1, status_ninho1 = calcular_receita_leite_po(quantidadeChocolate, quantidadeLeiteCondensado, quantidadeManteiga, quantidadeLeiteEmPo, valorChocolate, valorLeiteCondensado,valorManteiga, valorLeiteEmPo, aumentarReceita, valorUnitarioU)
        valor_da_receita2 ,valor_da_unidade2,valor_do_lucro2, status_cafe1 = calcular_receita_cafe(quantidadeChocolate, quantidadeLeiteCondensado, quantidadeManteiga, quantidadeCafe, valorChocolate, valorLeiteCondensado,valorManteiga, valorCafe, aumentarReceita, valorUnitarioU)
        valor_da_receita3 ,valor_da_unidade3,valor_do_lucro3, status_coco1 = calcular_receita_coco(quantidadeChocolate, quantidadeLeiteCondensado, quantidadeManteiga, quantidadeCoco, valorChocolate, valorLeiteCondensado,valorManteiga, valorCoco, aumentarReceita, valorUnitarioU)

        
        if status_ninho1 == False:
            status_ninho1 = "imgFALSE"
        else:
            status_ninho1 = "imgOK"

        if status_cafe1 == False:
            status_cafe1 = "imgFALSE"
        else:
            status_cafe1 = "imgOK"

        if status_coco1 == False:
            status_coco1 = "imgFALSE"
        else:
            status_coco1 = "imgOK"

        context = {
            'valor_da_receita1': f"{valor_da_receita1:.2f}",
            'valor_da_unidade1': valor_da_unidade1,
            'valor_do_lucro1': valor_do_lucro1,
            'status_ninho1': status_ninho1,

            'valor_da_receita2': f"{valor_da_receita2:.2f}",
            'valor_da_unidade2': valor_da_unidade2,
            'valor_do_lucro2': valor_do_lucro2,
            'status_cafe1': status_cafe1,
            
            'valor_da_receita3': f"{valor_da_receita3:.2f}",
            'valor_da_unidade3': valor_da_unidade3,
            'valor_do_lucro3': valor_do_lucro3,
            'status_coco1': status_coco1,   
        }
        return render(request, "ingredientes/resultados.html", context=context)

    return render(request, "ingredientes/resultados.html", context={})
