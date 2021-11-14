from vehicles import Vehicle
from errors import LowFuel, OverFuel

from dataclasses import dataclass


@dataclass
class Engine:
    fuel_consumption: float


class Car(Vehicle):
    autos = []

    def __init__(self,
                 year: int,
                 make: str,
                 model: str,
                 engine: Engine,
                 fuel_tank: int = 50
                 ):
        super().__init__(year, make, model)
        self.autos.append(self)
        self.engine = engine
        self.__fuel = 0.0
        self.fuel_tank = fuel_tank

    def __repr__(self):
        cls_name = type(self).__name__
        return (
            f'{cls_name}: {self.year} {self.make} {self.model}'
            f'{self.engine}'
        )

    def start(self):
        if self.__fuel > 0:
            print('The engine has started.')
        else:
            raise LowFuel()

    def stop(self):
        print('The engine has stopped.')

    def move_to(self, distance: float):
        fuel_consumed = distance / self.engine.fuel_consumption
        if fuel_consumed <= self.__fuel:
            self.__fuel -= fuel_consumed
            return distance
        else:
            raise LowFuel()

    @property
    def fuel_lvl(self):
        return self.__fuel

    def fill_gas_tank(self, fuel: float):
        temp_fuel = self.__fuel + fuel
        if temp_fuel <= self.fuel_tank:
            self.__fuel += fuel
        else:
            self.__fuel = self.fuel_tank
            raise OverFuel(f'The fuel tank is full, {temp_fuel - self.__fuel}\
                l petrol is lost.')

    @classmethod
    def cars_count(cls):
        return len(cls.autos)
