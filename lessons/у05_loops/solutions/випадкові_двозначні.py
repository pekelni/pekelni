import random

рядок_з_числами = ''
for i in range(20):
    перша_цифра = random.randint(1, 9)
    друга_цифра = перша_цифра
    while перша_цифра == друга_цифра:
        друга_цифра = random.randint(0, 9)
    число = перша_цифра * 10 + друга_цифра
    рядок_з_числами += str(число) + ' '

print(рядок_з_числами)
