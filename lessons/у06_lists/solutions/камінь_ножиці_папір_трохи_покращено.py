import random

КАМІНЬ, НОЖИЦІ, ПАПІР = 3, 2, 1
ПЕРШИЙ_ПЕРЕМАГАЄ = ((КАМІНЬ, НОЖИЦІ), (НОЖИЦІ, ПАПІР), (ПАПІР, КАМІНЬ))

людина = int(input('Введіть камінь (3), ножиці (2) або папір (1): '))
машини = random.randint(1, 3)

if людина == машини:
    переможець = 'ніхто'
elif (людина, машини) in ПЕРШИЙ_ПЕРЕМАГАЄ:
    переможець = 'людина'
else:
    переможець = 'машини'

if машини == КАМІНЬ:
    машини = 'камінь'
elif машини == НОЖИЦІ:
    машини = 'ножиці'
else:
    машини = 'папір'

print('Машини зробили ставку на ' + машини)

if переможець == 'людина':
    print('Ви перемогли, підступні плани машин не увінчалися успіхом, але не варто розслаблятися.')
elif переможець == 'машини':
    print('Ви програли. Термінатор вже виїхав.')
else:
    print('Сили людей и машин виявилися рівними цього разу.')
