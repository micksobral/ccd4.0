# faça um agoritmo para receber um numero qualquer e imprimir na tela se o nmr é
# par ou impar, positivo ou negativo

#arrumar

cont = 1
while cont != 2:

    numero = int(input("digite um numero: "))

    if numero % 2 == 0:
        if numero >=0:
            print(f"{numero}  é par e positivo")
        else:
            print(f"{numero} é par e negativo")
    else:
        if numero >= 0:
            print(f"{numero}  é ímpar e positivo")
        else:
            print(f"{numero} é ímpar e negativo")

    cont = int(input("quer continuar? digite: 1, se nao, digite: 2"))
    print("obrigado!")
