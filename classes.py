import classes_pack as cp

r20a2 = cp.Engine(10.0)
honda = cp.Car(55, r20a2)

try:
    honda.start()
except cp.LowFuel:
    print('The fuel tank is empty.')

honda.fuel_up(45)
honda.start()
honda.fuel_lvl
honda.fuel_up(10)

try:
    honda.move_to(10)
except cp.LowFuel:
    print('Not enough fuel.')

honda.fuel_lvl
try:
    honda.move_to(400)
except cp.LowFuel:
    print('Not enough fuel.')

honda.fuel_lvl
honda.stop()
