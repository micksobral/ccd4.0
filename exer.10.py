#recebe a primeira/segunda hora e o primeiro/segundo minuto
hora1 = int(input("digite o primeiro horario: "))
min1 = int(input("digite os minutos: "))
hora2 = int(input("digite o segundo horario: "))
min2 = int(input("digite os minutos: "))

#subtrair 12, caso hora1 ou hora2 for >12


if hora1 > 12:
  hora1 -= 12

if hora2 > 12:
  hora2 = hora2 - 12


  #pegar o resultado e verificar as horas sao maior que 12 e se as somas dos minutos sao maior que 60
  # caso seja maior que 12/60 subtrair -12/60



totalMin = min1 + min2
totalH = hora1 + hora2


if totalMin > 60:
  totalMin -= 60
  totalH += 1

if totalH > 12:
  totalH -= 12

print(f"{totalH}:{totalMin}")








