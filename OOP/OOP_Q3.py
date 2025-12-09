class animal():

    def speak(self):
        return "Animal sounds"
    
class dog(animal):

    def bark(self):
        return "bark"
    

d1 = dog()
print(d1.bark())  