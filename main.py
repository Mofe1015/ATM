from os import system
currency50 = 100
currency10 = 100
currency5 = 100
currency1 = 100

num = 1

contas = [["mofe", "matheus", "bruno", "jan"],
          ["1234", "4567", "8910", "1112"],
          [2000, 2000, 2000, 2000]]

while int(num) != 0:

    username = input('\n\nPlease enter your username: ')

    if username in contas[0]:

        amountGiven = 0
        givenNotes = []

        userPosition = contas[0].index(username)
        password = input('Please enter your password: ')
        system('cls')

        if password == contas[1][userPosition]:
            balance = contas[2][userPosition]

            print('\nWelcome', username)
            print('Your balance is $B', balance)

            num = int(input('\nPlease enter an amount to withdraw: '))
            print("\n")

            if balance >= num and num <= 1000:
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
                contas[2][userPosition] = newBalance

                for i in givenNotes:
                    print(i)

                print("\nSuccesfully withdrew B$", num)
                print('Your new balance is $B', newBalance)

            elif num > 1000:
                print("Exceeded $B1000 withdrawal limit")
            else:
                print("Sorry your balance is too low")
        else:
            print('Wrong password')
    else:
        print('Wrong username !!')
