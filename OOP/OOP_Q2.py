class Car:
  
    wheels = 4

    def __init__(self, color):
        self.color = color

car1 = Car("Red")
car2 = Car("Blue")

print(f"Initial State:")
print(f"Car 1 color (Instance Variable): {car1.color}")
print(f"Car 1 wheels (Class Variable): {car1.wheels}")
print(f"Car 2 color (Instance Variable): {car2.color}")
print(f"Car 2 wheels (Class Variable): {car2.wheels}")
print(f"Class Car wheels (Class Variable accessed via class): {Car.wheels}")

car1.wheels = 3

print(f"\nAfter changing car1.wheels to 3:")
print(f"Car 1 wheels (Instance Variable created on car1): {car1.wheels}")
print(f"Car 2 wheels (Still referencing Class Variable): {car2.wheels}")
print(f"Class Car wheels (Original Class Variable): {Car.wheels}")
