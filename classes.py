import traceback

from vehicles_pack import Car, Engine, LowFuel, OverFuel


r20a2 = Engine(10.0)
honda = Car(55, r20a2)

print(honda)

try:
    honda.start()
except LowFuel:
    print('The fuel tank is empty.')

honda.fuel_up(45)
print('The tank is filled up', honda.fuel_lvl, 'liters.')

honda.start()
print('{0} liters'.format(honda.fuel_lvl))
try:
    honda.fuel_up(100)
except OverFuel:
    print(traceback.format_exc())
print('The tank is filled up', honda.fuel_lvl, 'liters.')

try:
    print('The car has gone {0} kilometers'.format(honda.move_to(10)))
except LowFuel:
    print('Not enough fuel.')

print('{0} liters'.format(honda.fuel_lvl))

try:
    print('The car has gone {0} kilometers'.format(honda.move_to(400)))
except LowFuel:
    print('Not enough fuel.')

print('{0} liters'.format(honda.fuel_lvl))
honda.stop()

b2w = Engine(8.0)
vw = Car(55, b2w)
print('*' * 40)
print('Total', Car.cars_count(), 'cars:', *Car.autos)
