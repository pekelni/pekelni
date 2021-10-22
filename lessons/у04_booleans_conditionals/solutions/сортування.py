n0 = int(input('Введіть перше число: '))
n1 = int(input('Введіть друге число: '))
n2 = int(input('Введіть третє число: '))

if n0 > n1:
    n0, n1 = n1, n0

if n1 > n2:
    n1, n2 = n2, n1
    if n0 > n1:
        n0, n1 = n1, n0

print(n0, n1, n2)
