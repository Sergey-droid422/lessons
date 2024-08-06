import ephem

mars = ephem.Jupiter('2012/01/24')
print(mars)


cons = ephem.constellation(mars)

print(cons)


