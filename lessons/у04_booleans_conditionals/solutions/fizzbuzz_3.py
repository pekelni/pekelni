число = int(input('Введіть ціле число: '))
if число % 3 == 0:
    if число % 5 == 0:
        результат = 'FizzBuzz'
    else:
        результат = 'Fizz'
elif число % 5 == 0:
    результат = 'Buzz'
else:
    результат = str(число)
print('Результат: ' + результат)
