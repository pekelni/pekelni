import time

прості_числа = list()

рядок_для_друку = ''
start = time.time()
for число in range(2, 20_000):
    просте = True
    for дільник in прості_числа:
        if число % дільник == 0:
            просте = False
            break
        if дільник ** 2 > число:
            break
    if not просте:
        continue
    прості_числа.append(число)
    if len(прості_числа) % 200 == 0:
        рядок_для_друку += str(число) + ' '

тривалість = time.time() - start
print(рядок_для_друку)
print(f'Пошук простих чисел зайняв {round(тривалість, 2)} секунд')
