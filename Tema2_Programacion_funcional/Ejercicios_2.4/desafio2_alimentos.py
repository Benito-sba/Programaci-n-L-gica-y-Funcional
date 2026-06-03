//BENITO SANTIAGO BALAM ACEVEDO
//AA2.4


def preparar_pizza():
    return "🍕 pizza"

def preparar_hamburguesa ():
    return "🍔 hambruguesa"

def preparar_hotdog():
    return "🐕‍🦺 hotdog"

    

def cal_bonus(num_prociones):
    return "coca gratis" if num_prociones > 2 else ""


def ordenar_alimento(prepara_alimentos, numero_porciones):
    prociones_alimentos = [prepara_alimentos() for _ in range(numero_porciones)]
    bonus = cal_bonus(prociones_alimentos)
    return prociones_alimentos, bonus


encargo= [
    {"alimento": preparar_pizza, "cantidad": 2, "grupo": "Grupo A - Pizza"},
    {"alimento": preparar_hamburguesa, "cantidad": 10, "grupo": "Grupo B - Hamburguesa"},
    {"alimento": preparar_hotdog, "cantidad": 6, "grupo": "Grupo C - Hotdog"}
]

resultados = [
    {
        "grupo": orden["grupo"],
        "orden": ordenar_alimento(orden["alimento"], orden["cantidad"])[0],
        "bonus": ordenar_alimento(orden["alimento"], orden["cantidad"])[1]
    }
    for orden in encargo
]

for resultado in resultados:
    print(f"\n=== {resultado['grupo']} ===")
    print(f"Orden: {resultado['orden']}")
    print(f"Bonus: {resultado['bonus']}")


