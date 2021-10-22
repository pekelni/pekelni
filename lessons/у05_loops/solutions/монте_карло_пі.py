import random

TOTAL = 1_000_000
count = 0
for i in range(TOTAL):
    x = random.random()
    y = random.random()
    if x ** 2 + y ** 2 <= 1:
        count += 1
print(count / TOTAL * 4)
