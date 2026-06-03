//BENITO SANTIAGO BALAM ACEVEDO
//AA2.4

# 1 crear la funcion 

def preparar_cafe ():
    return "cafe"


def ordenar_cafe(numero_taza):
    tazas_cafe = [preparar_cafe() for _ in range(numero_taza)]
    return tazas_cafe

cafe_para_grupo = ordenar_cafe(10)

print(cafe_para_grupo)
