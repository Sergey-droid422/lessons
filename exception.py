import random


def cut_cake(people):
    try:
        z = 1 / people
        print(f'Каждый получит по {z} пирога')
    except (ZeroDivisionError, TypeError):
        print('Не могу поделить')



while True:
    people = random.randint(1, 10)
    cut_cake(people)
