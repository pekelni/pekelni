import random

РОЗМІР_ПОЛЯ = 3
ЗНАКИ = ('X', '0')
поле = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]

for номер_ходу in range(РОЗМІР_ПОЛЯ ** 2):
    поточний_знак = ЗНАКИ[номер_ходу % 2]
    while True:
        рядок, колонка = random.randint(0, 2), random.randint(0, 2)
        if not поле[рядок][колонка]:
            поле[рядок][колонка] = поточний_знак
            break

    for рядок in поле:
        for символ in рядок:
            print(символ or '_', end=' ')
        print()
    print()
