class Animal:
    def sound(self):
        print("Some sound\n")

class Dog(Animal):
    def sound(self):
        print("Bark!")



D=Dog()
D.sound()