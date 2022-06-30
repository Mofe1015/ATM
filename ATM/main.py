from os import system
from timeit import repeat
currency50 = 5
currency10 = 100
currency5 = 100
currency1 = 100
totalCurrency = 50*currency50 + 10*currency10 + 5*currency5 + 1*currency1
print("Total available currency is", totalCurrency)

repeat = True

contas = [["mofe", "matheus", "bruno", "jan", "conta4"],
          ["1234", "4567", "8910", "1112", "1314"],
          [2000, 2000, 2000, 2000]]

while repeat == True:

    username = input('\n\nPor favor insira seu nome de usuário: ')

    if username in contas[0]:

        amountGiven = 0
        givenNotes = []

        userPosition = contas[0].index(username)
        password = input('Por favor, insira sua senha: ')
        system('cls')

        if password == contas[1][userPosition]:
            balance = contas[2][userPosition]

            print('\nBem-vindo', username)
            print('Seu saldo é $B', balance)

            num = int(input('\nInsira um valor para sacar: '))
            print("\n")

            if balance >= num and num <= 1000 and totalCurrency > num:
                while amountGiven < int(num):
                    if currency50 > 0 and amountGiven+50 <= int(num):
                        givenNotes.append("B$50")
                        currency50 -= 1
                        amountGiven += 50
                    elif currency10 > 0 and amountGiven+10 <= int(num):
                        givenNotes.append("B$10")
                        currency10 -= 1
                        amountGiven += 10
                    elif currency5 > 0 and amountGiven+5 <= int(num):
                        givenNotes.append("B$5")
                        currency5 -= 1
                        amountGiven += 5
                    elif currency1 > 0 and amountGiven+1 <= int(num):
                        givenNotes.append("B$1")
                        currency1 -= 1
                        amountGiven += 1

                newBalance = balance - num
                totalCurrency -= num
                contas[2][userPosition] = newBalance

                for i in givenNotes:
                    print(i)

                print("\nSacou B$", num, "com sucesso !!")
                print('Seu novo saldo é de $B', newBalance)
            elif totalCurrency < num:
                print(
                    "Não há dinheiro suficiente no sistema para este saque, o total de dinheiro disponível é ", totalCurrency)
            elif num > 1000:
                print("Excedeu o limite de saque de $ B1000")
            else:
                print("Desculpe, seu saldo está muito baixo")
        else:
            print('Senha incorreta')
    else:
        print('Nome de usuário errado !!')
