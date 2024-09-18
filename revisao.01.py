#faça um aloritmo que leia os valores de A, B, C em seguida imprima na
# tela a soma entre A e B e motree se a soma é menor que C.

valor1 = int(input("digite uma valor: "))
valor2 = int(input("digite uma valor: "))
valor3 = int(input("digite uma valor: "))

soma = valor1 + valor2
if soma < valor3:
    print(f"{soma} é menor que {valor3}")

else:
    print(f"{soma}  é maior {valor3}")
