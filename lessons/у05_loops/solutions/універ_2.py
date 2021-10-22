РІЧНИЙ_МНОЖНИК = 1.038
поточна_річна_ціна = 50_000 * РІЧНИЙ_МНОЖНИК ** 10

сумарна_плата_через_10_років = 0
for _ in range(4):
    сумарна_плата_через_10_років += поточна_річна_ціна
    поточна_річна_ціна *= РІЧНИЙ_МНОЖНИК

print(f'Сумарна плата через 10 років складатиме: ${int(сумарна_плата_через_10_років)}')
