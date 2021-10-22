import time

start = time.time()
лічильник = 0
for число in range(2, 20_000):
    просте = True
    for дільник in range(2, число):
        if число % дільник == 0:
            просте = False
            break
    if not просте:
        continue
    лічильник += 1
    if лічильник % 200 == 0:
        print(число, end=' ')

тривалість = time.time() - start
print(f'\nПошук простих чисел зайняв {round(тривалість, 2)} секунд')
