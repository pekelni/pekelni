fz = int(input('Введіть ціле число: '))
if fz % 3 == 0 and fz % 5 == 0:
    fz = 'FizzBuzz'
elif fz % 3 == 0:
    fz = 'Fizz'
elif fz % 5 == 0:
    fz = 'Buzz'
print('Результат: ' + str(fz))
