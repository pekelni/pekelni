import time

число = 777_777
початковий_час = time.time()
результат_розрахунку = число ** число
тривалість = time.time() - початковий_час
приклад_як_рядок = str(число) + ' ** ' + str(число)
print('Розрахунок (' + приклад_як_рядок + ') зайняв ' + str(round(тривалість, 3)) + ' секунд')
