class Employee:

    def __init__(self,salary,name,bond):
        self.salary=salary #Create an instance attribute of name salary
                           #and assign it with salary
        self.name=name
        self.bond=bond

    def get_salary(self):
        return self.salary
    
    def info(self):
        print(f"The name of the employee is {self.name}, Salary is {self.salary} and bond is of {self.bond} years.")

e1=Employee(34000,"J.Gando",4)
print(e1.info())

e2=Employee(40000,"P.Bhando",2)
print(e2.info())

e3=Employee(36000,"KL.Chando",1)
print(e3.info())