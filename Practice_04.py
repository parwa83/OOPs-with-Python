class Train:
    def __init__(self,name,Coach,age,boarding_station,destination):
        self.name=name
        self.Coach=Coach
        self.age=age
        self.boarding_station=boarding_station
        self.destination=destination

    def book_ticket1(self):
        self.name=input("Enter your name")
        self.Coach=input("Enter the class AC/Sleeper/General")
        self.age=int(input("Enter your age"))
        self.boarding_station=input("Enter boarding_station")
        self.destination=input("Enter destination")

    def put_info(self):
        print(f"The name of passenger is {self.name} \n")
        print(f"The Coach of passenger is {self.Coach} \n")
        print(f"The age of passenger is {self.age} \n")
        print(f"The boarding station of passenger is {self.boarding_station} \n")
        print(f"The destination of passenger is {self.destination} \n")

    def get_status(self):
        ans=self.age*8
        print(f"Available trains from {self.boarding_station} to {self.destination} are:\n")
        print("Express / Superfast Trains :Rajdhani Express,Shatabdi Express,Duronto Express,Garib Rath Express,Sampark Kranti Express,Jan Shatabdi Express\n")
        print("Vande Bharat Express,Tejas Express,Humsafar Express,Antyodaya Express,Gatimaan Express,Maharaja Express\n")
        print("Mail Train,Express Passenger,MEMU,DEMU\n")
        print(f"No. of seats available are {ans}\n")

    def fare(sef):    #Changed self to sef,It still worked
        print("Unreserved / General (Passenger / MEMU / DEMU → ₹0.5 – ₹1 per km")
        print("Sleeper (SL)→ ₹0.6 – ₹1.2 per km")
        print("Second Sitting (2S)→ ₹0.7 – ₹1.3 per km")
        print("AC Chair Car (CC)→ ₹1.5 – ₹2.5 per km")
        print("AC 3 Tier (3A)→ ₹1.8 – ₹3 per km")
        print("AC 2 Tier (2A)→ ₹2.5 – ₹4 per km")
        print("AC 1st Class (1A)→ ₹4 – ₹6+ per km")


P1=Train('Parwa','AC',25,'Katni','Jabalpur')    #With constructor call
P1.put_info()
# P1=Train()              #Withourt Constructor
# P1.book_ticket1()       #Call
P1.get_status()
P1.fare()


