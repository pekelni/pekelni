бали = input('Введіть бали, розділені пробілом: ')
бали = бали.split()
if бали:
    кращий_бал = None
    for i in range(len(бали)):
        бали[i] = int(бали[i])
        if not кращий_бал or бали[i] > кращий_бал:
            кращий_бал = бали[i]

    for i in range(len(бали)):
        if бали[i] >= кращий_бал - 10:
            оцінка = 'A'
        elif бали[i] >= кращий_бал - 20:
            оцінка = 'B'
        elif бали[i] >= кращий_бал - 30:
            оцінка = 'C'
        elif бали[i] >= кращий_бал - 40:
            оцінка = 'D'
        else:
            оцінка = 'F'
        print(f'У студента #{i} {бали[i]} балів, а оцінка - {оцінка}')
