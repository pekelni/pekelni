РОЗМІР_ДОШКИ = 8

ПУСТИЙ_РЯДОК = list()
for i in range(РОЗМІР_ДОШКИ):
    ПУСТИЙ_РЯДОК.append(False)

for різниця in range(1 - РОЗМІР_ДОШКИ, РОЗМІР_ДОШКИ):
    print()
    дошка = list()
    for i in range(РОЗМІР_ДОШКИ):
        дошка.append(list(ПУСТИЙ_РЯДОК))

    for i in range(РОЗМІР_ДОШКИ):
        for j in range(РОЗМІР_ДОШКИ):
            if i - j == різниця:
                дошка[i][j] = True

    for рядок in дошка:
        print(end='|')
        for клітина in рядок:
            символ = 'D' if клітина else ' '
            print(символ, end='|')
        print()

for сума in range(2 * РОЗМІР_ДОШКИ - 1):
    print()
    дошка = list()
    for i in range(РОЗМІР_ДОШКИ):
        дошка.append(list(ПУСТИЙ_РЯДОК))

    for i in range(РОЗМІР_ДОШКИ):
        for j in range(РОЗМІР_ДОШКИ):
            if i + j == сума:
                дошка[i][j] = True

    for рядок in дошка:
        print(end='|')
        for клітина in рядок:
            символ = 'D' if клітина else ' '
            print(символ, end='|')
        print()
