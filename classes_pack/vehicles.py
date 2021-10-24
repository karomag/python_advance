from abc import ABC, abstractmethod


class Vehicle(ABC):

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
    def fuel_up(self, fuel):
        pass
