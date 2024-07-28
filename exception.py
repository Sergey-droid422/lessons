

def cut_cake(people):
    try:
        z = 1 / people
        print(f'Каждый получит по {z} пирога')
    except ZeroDivisionError:
        print('Не могу поделить на 0')

cut_cake(0)