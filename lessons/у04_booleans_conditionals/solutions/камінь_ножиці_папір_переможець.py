КАМІНЬ, НОЖИЦІ, ПАПІР = 3, 2, 1

гравець_1 = int(input('Що загадав перший гравець? Введіть камінь (3), ножиці (2) або папір (1): '))
гравець_2 = int(input('Що загадав ДРУГИЙ гравець? Введіть камінь (3), ножиці (2) або папір (1): '))

if гравець_1 == гравець_2:
    переможець = 'ніхто'
elif гравець_1 == КАМІНЬ and гравець_2 == НОЖИЦІ:
    переможець = 'перший гравець'
elif гравець_1 == НОЖИЦІ and гравець_2 == ПАПІР:
    переможець = 'перший гравець'
elif гравець_1 == ПАПІР and гравець_2 == КАМІНЬ:
    переможець = 'перший гравець'
else:
    переможець = 'другий гравець'

if переможець == 'ніхто':
    print('Нічия')
else:
    print('Переміг ' + переможець)
