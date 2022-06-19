
currency50 = 100
currency10 = 100
currency5 = 100
currency1 = 100

num = 1

contas = [["mofe", "matheus", "bruno", "jan"],
          ["1234", "4567", "8910", "1112"],
          [2000, 2000, 2000, 2000]]

while int(num) != 0:

    username = input('Please enter your username: ')

    if username in contas[0]:

        amountGiven = 0
        givenNotes = []

        userPosition = contas[0].index(username)
        password = input('Please enter your password: ')

        if password == contas[1][userPosition]:
            balance = contas[2][userPosition]

            print('Welcome', username)
            print('Your balance is $B', balance)

            num = int(input('Please enter an ammount: '))

            if balance > num:
                while amountGiven < int(num):
                    if currency50 > 0 and amountGiven+50 <= int(num):
                        givenNotes.append(50)
                        currency50 -= 1
                        amountGiven += 50
                    elif currency10 > 0 and amountGiven+10 <= int(num):
                        givenNotes.append(10)
                        currency10 -= 1
                        amountGiven += 10
                    elif currency5 > 0 and amountGiven+5 <= int(num):
                        givenNotes.append(5)
                        currency5 -= 1
                        amountGiven += 5
                    elif currency1 > 0 and amountGiven+1 <= int(num):
                        givenNotes.append(1)
                        currency1 -= 1
                        amountGiven += 1

                newBalance = balance - num
                contas[2][userPosition] = newBalance

                print('\n\nYour new balance is $B', newBalance)
                print(givenNotes)
                print(sum(givenNotes))
            else:
                print("Sorry your balance is too low")
        else:
            print('Wrong password')
    else:
        print('Wrong username !!')
