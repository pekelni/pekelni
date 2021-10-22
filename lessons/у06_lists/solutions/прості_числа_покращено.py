import time

прості_числа = list()

start = time.time()
for число in range(2, 20_000):
    просте = True
    for дільник in прості_числа:
        if число % дільник == 0:
            просте = False
            break
    if not просте:
        continue
    прості_числа.append(число)
    if len(прості_числа) % 200 == 0:
        print(число, end=' ')

тривалість = time.time() - start
print(f'\nПошук простих чисел зайняв {round(тривалість, 2)} секунд')
