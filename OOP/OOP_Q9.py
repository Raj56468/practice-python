class animal():
    def __init__(self,name):
        self.name = name

class dog(animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog1 = dog("Buddy", "Golden Retriever")
print(dog1.name)
print(dog1.breed)