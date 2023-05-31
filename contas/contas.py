def verifica_qt_choco(quantChoc):
    return quantChoc >= 400

def verifica_qt_leiteC(quantLeiteC):
    return quantLeiteC >= 395

def verifica_qt_matega(quantMant):
    return quantMant >= 40

def verifica_qt_po(quantLeiteP):
    return quantLeiteP >= 50

def verifica_qt_coco(quantCoco):
    return quantCoco >= 300

def verifica_qt_Cafe(quantCafe):
    return quantCafe >= 100

def calcular_receita_leite_po(quantChoc, quantLeiteC, quantMant, quantLeiteP, precoChoc, precoLeiteC, precoMant, precoLeiteP, aumentarReceita, valorUnitarioU):
    if verifica_qt_matega(quantMant) and verifica_qt_choco(quantChoc) and verifica_qt_leiteC(quantLeiteC) and verifica_qt_po(quantLeiteP):
        status = True
        precoReceitaLeitePo = ((precoChoc / quantChoc) * 400 + (precoLeiteC / quantLeiteC) * 395 + (precoMant / quantMant) * 40 + (precoLeiteP / quantLeiteP) * 50) * aumentarReceita
        valorUnitarioLeitePo = precoReceitaLeitePo / (50 * aumentarReceita)
        valorUnitarioSugeridoLeitePo = valorUnitarioU
        lucro = valorUnitarioSugeridoLeitePo * (50 * aumentarReceita) - precoReceitaLeitePo
        print(f"Receita de leite em pó: R${precoReceitaLeitePo}, valor da unidade: R${valorUnitarioLeitePo}, Lucro: R${lucro}")
        if precoReceitaLeitePo > (60 * aumentarReceita):
            status=False
        return precoReceitaLeitePo,valorUnitarioLeitePo,lucro,status
    else:
        precoReceitaLeitePo = 0
        valorUnitarioLeitePo= 0
        lucro = 0
        status = False
        return precoReceitaLeitePo,valorUnitarioLeitePo,lucro,status
def calcular_receita_cafe(quantChoc, quantLeiteC, quantMant, quantCafe, precoChoc, precoLeiteC, precoMant, precoCafe, aumentarReceita, valorUnitarioU):
    if verifica_qt_matega(quantMant) and verifica_qt_choco(quantChoc) and verifica_qt_leiteC(quantLeiteC) and verifica_qt_Cafe(quantCafe):
        status = True
        precoReceitaCafe = ((precoChoc / quantChoc) * 400 + (precoLeiteC / quantLeiteC) * 395 + (precoMant / quantMant) * 40 + (precoCafe / quantCafe) * 100) * aumentarReceita
        valorUnitarioCafe = precoReceitaCafe / (50 * aumentarReceita)
        valorUnitarioSugeridoCafe = valorUnitarioU
        lucro = valorUnitarioSugeridoCafe * (50 * aumentarReceita) - precoReceitaCafe
        print(f"Receita de Café: R${precoReceitaCafe}, valor da unidade: R${valorUnitarioCafe}, Lucro: R${lucro}")
        if precoReceitaCafe > (60 * aumentarReceita):
            status=False
        return precoReceitaCafe,valorUnitarioCafe,lucro,status
    else:
        precoReceitaCafe = 0
        valorUnitarioCafe= 0
        lucro = 0
        status = False
        return precoReceitaCafe,valorUnitarioCafe,lucro,status
def calcular_receita_coco(quantChoc, quantLeiteC, quantMant, quantCoco, precoChoc, precoLeiteC, precoMant, precoCoco, aumentarReceita, valorUnitarioU):
    if verifica_qt_matega(quantMant) and verifica_qt_choco(quantChoc) and verifica_qt_leiteC(quantLeiteC) and verifica_qt_coco(quantCoco):
        status = True
        precoReceitaCoco = ((precoChoc / quantChoc) * 400 + (precoLeiteC / quantLeiteC) * 395 + (precoMant / quantMant) * 40 + (precoCoco / quantCoco) * 300) * aumentarReceita
        valorUnitarioCoco = precoReceitaCoco / (50 * aumentarReceita)
        valorUnitarioSugeridoCoco = valorUnitarioU
        lucro = valorUnitarioSugeridoCoco * (50 * aumentarReceita) - precoReceitaCoco
        print(f"Receita de Coco: R${precoReceitaCoco}, valor da unidade: R${valorUnitarioCoco}, Lucro: R${lucro}")

        if precoReceitaCoco > (60 * aumentarReceita):
            status=False
        return precoReceitaCoco,valorUnitarioCoco,lucro,status

    else:
        precoReceitaCoco = 0
        valorUnitarioCoco= 0
        lucro = 0
        status = False
        return precoReceitaCoco,valorUnitarioCoco,lucro,status