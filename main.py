time1 = time2 = 0
soma = 0

while True:
    ganhou = int(input("Digite 1 para o 1ºtime e 2 para o 2ºtime: "))
    if ganhou == 1:
        time1 += 1
    if ganhou == 2:
        time2 += 1
    truco = str(input("Digite se foi Truco[S/N]"))
    if truco == 'S':
        soma +=1
        if ganhou == 1:
            time1 += 2
        if ganhou == 2:
            time2 += 2


    if truco == 'N':
        print()

    print(f"O time 1 tem {time1} pontos \n"
          f"e o time 2 tem {time2} pontos \n"
          f" e foi pedidos {soma} TRUCOS")
    print("-------"*4)
