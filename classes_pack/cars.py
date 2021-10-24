from vehicles import Vehicle
from errors import LowFuel

from dataclasses import dataclass


@dataclass
class Engine:
    fuel_consumption: float


class Car(Vehicle):

    def __init__(self, fuel_tank: int, engine: Engine):
        self.engine = engine
        self.__fuel_consumption = engine.fuel_consumption
        self.__fuel = 0.0
        self.fuel_tank = fuel_tank

    def start(self):
        if self.__fuel > 0:
            print('The engine has started.')
        else:
            raise LowFuel()

    def stop(self):
        print('The engine has stopped.')

    def move_to(self, distance: float):
        fuel_consumed = distance / self.__fuel_consumption
        if fuel_consumed <= self.__fuel:
            print('The car has gone {0} kilometers'.format(distance))
            self.__fuel -= fuel_consumed
        else:
            raise LowFuel()

    @property
    def fuel_lvl(self):
        print('{0} liters'.format(self.__fuel))

    def fuel_up(self, fuel: float):
        temp_fuel = self.__fuel + fuel
        if temp_fuel <= self.fuel_tank:
            self.__fuel += fuel
            print('The tank is filled up', fuel, 'liters.')
        else:
            self.__fuel = self.fuel_tank
            print('The fuel tank is full, {0}l petrol is lost.'.format(
                temp_fuel - self.__fuel
            ))
