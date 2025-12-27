class Calculator:
    
    def __init__(self):
        print("Hello")
    
    def get_num(self):
        self.num=int(input(print("Enter number")))

    def square(self):
        ans1=(self.num)*(self.num)
        return ans1
        
    def cube(self):
        ans2=(self.num)*(self.num)*(self.num)
        return ans2
    
N=Calculator()
N.get_num()
print(N.square())
print(N.cube())