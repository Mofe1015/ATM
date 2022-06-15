from contextlib import nullcontext
from locale import currency


print('Hello Worlds')
currency50 = 1000
currency20 = 1000
currency10 = 1000
currency5 = 1000

num = (input('Please enter an ammount: '))
amountGiven = 0
givenNotes = []

while amountGiven < int(num):

    if currency5 > 0 and amountGiven+5 <= int(num):
        givenNotes.append(5)
        currency5 - 1
        amountGiven += 5
    elif currency10 > 0 and amountGiven+1 <= int(num):
        givenNotes.append(1)
        currency10 - 1
        amountGiven += 1

print(givenNotes)
print(sum(givenNotes))
