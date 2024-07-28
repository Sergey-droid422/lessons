from if_operator import discounted



for number in range(3):
    print(f'Привет мир {number}!')


for letter in 'python':
    print(letter.title())


exemple_string = 'Я изучаем язык Python'

for word in exemple_string.split():
    print(f'Длинна слова "{word}": {len(word)}')


students_scores = [1, 21, 19, 6, 5]
sum_scors = 0


for score in students_scores:
    sum_scors += score

print(f'Средняя оценка студента : {sum_scors / len(students_scores)}')

stock = [
    {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 25},
    {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 10},
    {'name': '', 'stock': 15, 'price': 16112.1, 'discount': 25},

]



for phone in stock:
    phone['final_price'] = discounted(phone['price'], phone['discount'], name=phone['name'])
    






    