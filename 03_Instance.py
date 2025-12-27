class Employee:
    company="Tesla"   #Class attribute

    def __init__(self,salary,name,bond,company):
        self.salary=salary #Create an instance attribute of name salary
                           #and assign it with salary
        self.name=name
        self.bond=bond
        self.company=company

    def get_salary(self):
        return self.salary
    
    def info(self):
        print(f"The name of the employee is {self.name}, Salary is {self.salary} and bond is of {self.bond} years.")

e1 =Employee(3400,'Jhodo',3,'HP')   #Here HP is instance attribute
print(e1.company)  #What will it print class company or instance company?
#It'll always and always print instance attribute when its present,
#When not class attribute wil be printed.
#To print class attribute:
print(Employee.company)

#Object instropection: Tells about all the methods,instance that an object has.
print(dir(e1))