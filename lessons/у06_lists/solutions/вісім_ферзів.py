import random

РОЗМІР_ДОШКИ = 8
дошка = list()
ПУСТИЙ_РЯДОК = list()
for j in range(РОЗМІР_ДОШКИ):
    ПУСТИЙ_РЯДОК.append(False)
for i in range(РОЗМІР_ДОШКИ):
    рядок = list(ПУСТИЙ_РЯДОК)
    рядок[i] = True
    дошка.append(рядок)

лічильник_спроб = 0
while True:
    random.shuffle(дошка)
    лічильник_спроб += 1

    рішення_знайдене = True
    for сума in range(РОЗМІР_ДОШКИ * 2 - 1):
        ферзів_на_діагоналі = 0
        for i in range(РОЗМІР_ДОШКИ):
            for j in range(РОЗМІР_ДОШКИ):
                if i + j == сума:
                    ферзів_на_діагоналі += дошка[i][j]
        if ферзів_на_діагоналі > 1:
            рішення_знайдене = False

    for різниця in range(1 - РОЗМІР_ДОШКИ, РОЗМІР_ДОШКИ):
        ферзів_на_діагоналі = 0
        for i in range(РОЗМІР_ДОШКИ):
            for j in range(РОЗМІР_ДОШКИ):
                if i - j == різниця:
                    ферзів_на_діагоналі += дошка[i][j]
        if ферзів_на_діагоналі > 1:
            рішення_знайдене = False

    if рішення_знайдене:
        break

print(f'Пошук зайняв {лічильник_спроб} спроб')
for рядок in дошка:
    print(end='|')
    for клітина in рядок:
        символ = 'Q' if клітина else ' '
        print(символ, end='|')
    print()
