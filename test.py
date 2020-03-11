withdraw = int(input("Value: "))
banknotes = {5: 100, 10: 40, 50: 800}
bank = 0

for value in banknotes:
    bank += value * banknotes[value]

if withdraw > bank:
    print('There is not enough cash in the ATM')
elif withdraw % 5 != 0:
    print('The value must be a multiple of 5')
else:
    cash = {}
    for value in list(banknotes.keys())[::-1]:
        if withdraw // value != 0:
            if withdraw >= value*banknotes[value]:
                cash[value] = banknotes[value]
                withdraw -= value * banknotes[value]
            else:
                cash[value] = withdraw // value
                withdraw -= value * (withdraw // value)
    print("cash", cash)
