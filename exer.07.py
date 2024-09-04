time1 = input("digite o nome do time1: ")
placar1 = int(input(f"quantos gols {time1}: "))

time2 = input("digite o nome don time2")
placar2 = int(input(f"quantos gols{time2}: "))

if placar1==placar2:

    print("partida empatada")

elif placar1>placar2:
    print(f"0{time1} foi o vencedor")

else:
    print(f"0{time2}é o vencedor")