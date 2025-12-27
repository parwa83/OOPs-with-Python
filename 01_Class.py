#Class: Its a blueprint or template wgich allows different types of data members and
#its associated member functions to binde in single unit called class.Memory is ob]nly allocated
#when the objects are created.

#Eg: Form for a class that contains name,age,electives,father's naem etc.

#Object: Class variable or specific instance created from the class.

#Eg:Form for a person Gando is an object. 

class Employee:
    company="HP"

    def get_salary(self):  #'self' here references to the object of the class created/called
        return 34000

e=Employee() #e is the object of class Employee.
print(e.get_salary()) #Employee e's get_salary method is called

e2=Employee()
print(e2.get_salary())
print(e2.company)