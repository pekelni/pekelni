import itertools
import random

РОЗМІР_ПОЛЯ = 3
ЗНАКИ = ('X', '0')
поле = [[None for _ in range(РОЗМІР_ПОЛЯ)] for _ in range(РОЗМІР_ПОЛЯ)]
координати_клітинок = list(itertools.product(range(РОЗМІР_ПОЛЯ), range(РОЗМІР_ПОЛЯ)))
random.shuffle(координати_клітинок)

for номер_ходу, (рядок, колонка) in enumerate(координати_клітинок):
    поле[рядок][колонка] = ЗНАКИ[номер_ходу % 2]
    for рядок in поле:
        print(' '.join(символ or '_' for символ in рядок))
    print()
