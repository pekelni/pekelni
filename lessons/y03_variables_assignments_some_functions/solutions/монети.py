сума = int(input('Введіть суму: '))

кількість_монет_по_50 = сума // 50
сума %= 50
print('Монет по 50 копійок: ' + str(кількість_монет_по_50))

кількість_монет_по_25 = сума // 25
сума %= 25
print('Монет по 25 копійок: ' + str(кількість_монет_по_25))

кількість_монет_по_10 = сума // 10
сума %= 10
print('Монет по 10 копійок: ' + str(кількість_монет_по_10))

кількість_монет_по_5 = сума // 5
сума %= 5
print('Монет по 5 копійок: ' + str(кількість_монет_по_5))

print('Монет по 1 копійці: ' + str(сума))
