import traceback

import classes_pack as cp


r20a2 = cp.Engine(10.0)
honda = cp.Car(55, r20a2)

print(honda)

try:
    honda.start()
except cp.LowFuel:
    print('The fuel tank is empty.')

honda.fuel_up(45)
print('The tank is filled up', honda.fuel_lvl, 'liters.')

honda.start()
print('{0} liters'.format(honda.fuel_lvl))
try:
    honda.fuel_up(100)
except cp.OverFuel:
    print(traceback.format_exc())
print('The tank is filled up', honda.fuel_lvl, 'liters.')

try:
    print('The car has gone {0} kilometers'.format(honda.move_to(10)))
except cp.LowFuel:
    print('Not enough fuel.')

print('{0} liters'.format(honda.fuel_lvl))

try:
    print('The car has gone {0} kilometers'.format(honda.move_to(400)))
except cp.LowFuel:
    print('Not enough fuel.')

print('{0} liters'.format(honda.fuel_lvl))
honda.stop()
