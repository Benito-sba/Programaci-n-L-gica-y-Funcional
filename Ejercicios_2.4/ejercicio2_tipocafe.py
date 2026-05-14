//BENITO SANTIAGO BALAM ACEVEDO
//AA2.4

def preparar_cafe_americano ():
    return "cafe_americano"


def preparar_cafe_olla ():
    return "cafe_olla"


def ordenar_cafe(prepara_cafe, numero_taza):
    tazas_cafe = [prepara_cafe() for _ in range(numero_taza)]
    return tazas_cafe

grupoA = ordenar_cafe(preparar_cafe_americano, 15)

GrupoB = ordenar_cafe(preparar_cafe_olla, 13)

print(grupoA, GrupoB)