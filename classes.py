import traceback

from vehicles_pack import Car, Engine, LowFuel, OverFuel


r20a2 = Engine(10.0)
honda = Car(2011, 'Honda', 'CR-V', r20a2, fuel_tank=55)

print(honda)

try:
    honda.start()
except LowFuel:
    print('The fuel tank is empty.')

honda.fill_gas_tank(45)
print('The tank is filled up', honda.fuel_lvl, 'liters.')

honda.start()
print(f'{honda.fuel_lvl} liters')
try:
    honda.fill_gas_tank(100)
except OverFuel:
    print(traceback.format_exc())
print('The tank is filled up', honda.fuel_lvl, 'liters.')

try:
    print(f'The car has gone {honda.move_to(10)} kilometers')
except LowFuel:
    print('Not enough fuel.')

print(f'{honda.fuel_lvl} liters')

try:
    print(f'The car has gone {honda.move_to(400)} kilometers')
except LowFuel:
    print('Not enough fuel.')

print(f'{honda.fuel_lvl} liters')
honda.stop()

b2w = Engine(8.0)
vw = Car(2020, 'VW', 'Polo', b2w)
print('*' * 40)
print('Total', Car.cars_count(), 'cars:', *Car.autos)
