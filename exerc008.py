litros = float(input("informe quantos litros foram abastecidos"))
tipo = input("qual combustibel:")

if tipo == "G" or tipo == "g":
    valor = 5.8 * litros
    print(f"voce abasteceu {litros} e gastou {valor}")

elif tipo == "E" or tipo == "e":
    valor = 4.9
    print(f"voce abasteceu {litros} e gastou {valor}")

else:

    print("combustivel invalido")
