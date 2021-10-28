from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def move_to(self, distance):
        pass

    @property
    @abstractmethod
    def fuel_lvl(self):
        pass

    @abstractmethod
    def fill_gas_tank(self, fuel):
        pass
