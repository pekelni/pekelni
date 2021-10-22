import random

for i in range(6):
    число = str(random.randint(1, 9))
    while len(число) < 6:
        цифра = str(random.randint(0, 9))
        if цифра not in число:
            число += цифра
    print(число, end=' ')
