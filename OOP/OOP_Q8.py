from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self,can_start=True):
        if can_start:
            return "Vroom Vroom"

    @abstractmethod
    def stop(self,can_stop=True):
        if can_stop:
            return "can stop"

class bike(vehicle):
    def start(self, can_start=True):
        return super().start(can_start)

    def stop(self, can_stop=True):
        return super().stop(can_stop)

class car(vehicle):
    def start(self, can_start=True):
        return super().start(can_start)

    def stop(self, can_stop=True):
        return super().stop(can_stop)
    
bike1 = bike()
car1 = car()

print(bike1.start())
print(bike1.stop())
print(car1.start())
print(car1.stop())
        
