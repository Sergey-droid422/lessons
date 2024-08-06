from collections import Counter


phones = ['iPhone Xs', 'Samsung Galaxy S10', 'Xiaomi M18', 'iPhone Xs', 'iPhone Xs', 'iPhone Xs', 'Samsung Galaxy S10', 'Samsung Galaxy S10', 'Samsung Galaxy S10', 'Xiaomi M18']
count = Counter(phones)

print(count)

print(count['iPhone Xs'])
