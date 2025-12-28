class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def put_info(self):
        print(f"The person's name is {self.name} and age is {self.age}")

P=Person("Kishore",8)
P.put_info()
print(P.name,P.age) #Alternative way to print without put info function.