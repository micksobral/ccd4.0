
peso = float(input("digite see peso: "))
altura = float(input("digite sua altura: "))

calculo = peso / (altura ** 2)

if calculo  < 18.5:
    print("abaixo do peso")

elif calculo >= 18.6 and calculo <= 24.9:
    print("peso ideal. parabens")

elif calculo >= 25.0 and  calculo <= 29.9:
    print("levemente acima do peso")

elif calculo >= 30.0 and calculo <= 34.9:
    print("obesidade grau I")

elif calculo >= 35.0 and calculo <= 39.9:
    print("obesidade grau II(severa)")

elif calculo >= 40:
    print("obesidade grau III(mórbida)")

