class Parent():
    def show(self):
        print("Parent show")

class Child(Parent):
    def show(self):
        super().show()
        print("Child show")


Child().show()