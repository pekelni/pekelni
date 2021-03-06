РОЗМІР_ДОШКИ = 8

ПУСТИЙ_РЯДОК = list()
for i in range(РОЗМІР_ДОШКИ):
    ПУСТИЙ_РЯДОК.append(False)

МЕТА_ПАРАМЕТРИ = (
    ('різниця', range(1 - РОЗМІР_ДОШКИ, РОЗМІР_ДОШКИ)),
    ('сума', range(2 * РОЗМІР_ДОШКИ - 1)),
)

for тип_діагоналі, діапазон in МЕТА_ПАРАМЕТРИ:
    for параметр_діагоналі in діапазон:
        print()
        дошка = list()
        for i in range(РОЗМІР_ДОШКИ):
            дошка.append(list(ПУСТИЙ_РЯДОК))

        for i in range(РОЗМІР_ДОШКИ):
            for j in range(РОЗМІР_ДОШКИ):
                if тип_діагоналі == 'сума':
                    if i + j == параметр_діагоналі:
                        дошка[i][j] = True
                elif тип_діагоналі == 'різниця':
                    if i - j == параметр_діагоналі:
                        дошка[i][j] = True

        for рядок in дошка:
            print(end='|')
            for клітина in рядок:
                символ = 'D' if клітина else ' '
                print(символ, end='|')
            print()

