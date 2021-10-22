import random

поле = ['X'] * 5 + ['0'] * 4
random.shuffle(поле)
for i in range(len(поле)):
    print(поле[i], end=' ')
    if i % 3 == 2:
        print()
