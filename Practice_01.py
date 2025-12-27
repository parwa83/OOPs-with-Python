class Programmer:
    company="Microsoft"

    def get_info(self):
         self.name=input(print("Enter name of the employee"))
         self.salary=int(input(print("Enter salary of the employee")))

    def print_info(self):
         print(f"The name of employee at microsoft is {self.name} and salary is {self.salary}")

M=Programmer()
M.get_info()
M.print_info()
        
