class Animal:  #Parent class
    def __init__(self,name):
        self.name=name
        print(self.name)
    def speak(self):
        print("Generic animal sound")

class Dog(Animal): #This is how inheritence is done in python.
    def speak(self):
        super().speak()   #This calls base(Animal) class speak function.
        print("Woof!")


# a=Animal("Dog")
# a.speak()

d=Dog("Tommy")  #Here Dog class object 'd' is calling animal class constructor def __init__
d.speak()       #This overrides Animal class speak and calls Dog class speak, As dog class object is calling.