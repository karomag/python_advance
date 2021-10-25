from vehicles import Vehicle
from errors import LowFuel, OverFuel

from dataclasses import dataclass


@dataclass
class Engine:
    fuel_consumption: float


class Car(Vehicle):

    def __init__(self, fuel_tank: int, engine: Engine):
        self.engine = engine
        self.fuel_consumption = engine.fuel_consumption
        self.__fuel = 0.0
        self.fuel_tank = fuel_tank

    def __str__(self):
        cls_name = type(self).__name__
        return '{0} ({1})'.format(cls_name, self.engine)

    def start(self):
        if self.__fuel > 0:
            print('The engine has started.')
        else:
            raise LowFuel()

    def stop(self):
        print('The engine has stopped.')

    def move_to(self, distance: float):
        fuel_consumed = distance / self.fuel_consumption
        if fuel_consumed <= self.__fuel:
            self.__fuel -= fuel_consumed
            return distance
        else:
            raise LowFuel()

    @property
    def fuel_lvl(self):
        return self.__fuel

    def fuel_up(self, fuel: float):
        temp_fuel = self.__fuel + fuel
        if temp_fuel <= self.fuel_tank:
            self.__fuel += fuel
        else:
            self.__fuel = self.fuel_tank
            raise OverFuel('The fuel tank is full, {0}l petrol is lost.'.
                           format(temp_fuel - self.__fuel)
                           )
