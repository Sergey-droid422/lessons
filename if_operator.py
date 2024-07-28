balance = 100
price = 200


if price > balance:
    print('Пополните баланс !')
else:
    print('Приятных покупок!')





def weather(temperature):
    if temperature <= 0:
        return f'на улице холодно! {i} градусов'
    elif 1 <= temperature <= 15:
        return f'Наулице прохладно! {i} градусов'
    elif 16 <= temperature <= 25:
        return f'На улице тепло! {i} градусов'
    else:
        return f'на улице жарко! {i} градусов'
    

for i in range(34):
    print(weather(i))


phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 25}
phone2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 10}
phone3 = {'name': '', 'stock': 15, 'price': 16112.1, 'discount': 25}


def discounted(price, discount, max_discount=20, name=''):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount > 99:
        raise ValueError('Максимальная скидка не должна быть больше 100')
    if discount  >= max_discount or 'iphone' in name.lower() or not name:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    return price_with_discount


apple_disc = discounted(phone1['price'],phone1['discount'],name=phone1['name'])
print(apple_disc)

android_disc = discounted(phone2['price'],phone2['discount'],name=phone2['name'])
print(android_disc)

noname_disc = discounted(phone3['price'],phone3['discount'],name=phone3['name'])
print(android_disc)



 