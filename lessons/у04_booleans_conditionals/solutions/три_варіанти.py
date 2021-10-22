import random

ймовірність = random.random()
if ймовірність < 0.5:
    print('зрада')
elif ймовірність < 0.9:
    print('мутно')
else:
    print('ПЕРЕМОГА')
