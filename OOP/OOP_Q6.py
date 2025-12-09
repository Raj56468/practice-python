class Flyer():

    def fly(self):
        return "I can fly!"

class Swimmer():

    def swim(self):
        return "I can swim!"

class Duck(Flyer, Swimmer):

    def can_do_both(self):
        return f"{self.fly()} and {self.swim()}"

duck = Duck()
print(duck.can_do_both())
print(isinstance(duck, Flyer))
print(isinstance(duck, Swimmer))