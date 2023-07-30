from user import *
class Counter(waqas):
    user_list=[]
    def reservstion(self):
        bus_no=input("Enter bus number:")
        for bus in self.total_bus_list:
            if bus_no==["coach"]:
                passanger=input("Enter your name:")
                seat_no=int(input("Enter seat No :"))
                if seat_no >40:
                    print("No seat are avilable:")
                elif bus ["seat"][seat_no-1]!="Empty":
                    print("Seat is Already booked")
                else:
                    bus["seat"][seat_no-1]=passanger
            else:
                print("No bus avilabile")
                
        for bus in self.total_bus_list:
            print(bus['seat']) 
    def show_ticket(self):
        bus_no=int(input("Enter bus NO:"))

        for bus in self.total_bus_list:
            if bus_no == bus["coach"]:
                print ("*"*50)
                print()
                print(f"{''*10}{'#'*10} Bus INFO{'#'*10}")
                print(f"Bus Number:{bus_no}\t\t Driver : {bus['driver']}")
                print(f"Arrival:{bus['arrival']}\t\t Departure : {bus['departure']}")
                print(f"From:{bus['from_des']}\t\t TO : {bus['to']}")
                print()

                a=1
                for i in range(5):
                    for j in range (2):
                        print(f"{a}.{bus['seat'][a-1]}",end="\t")
                        a+=1
                    for j in range(2):
                            print(f"{a}.{bus['seat'][a-1]}",end="\t")
                            a+=1
                    print()
                print('*'*50)
    def get_users(self):
        return self.user_list
    def create_Account(self):
        name=input("Enter your user name:")
        password=input("Enter your password")
        self.new_user=User(name,password)
        self.user_list.append(vars(self.new_user))
    def Avilable_buses(self):
        if len(self.total_bus_list)==0:
            print("No bus avilable:\n")
        else:
            print('*'*50)
            for bus in self.total_bus_list:
                print()
                print(f"{''*10}{'#'*10} Bus INFO{'#'*10}")
                print(f"Bus Number:{bus['coach']}\t\t Driver : {bus['driver']}")
                print(f"Arrival:{bus['arrival']}\t\t Departure : {bus['departure']}")
                print(f"From:{bus['from_des']}\t\t TO : {bus['to']}")
                print()
while True:
    company=waqas()
    b=Counter()
    print("1. Create An Account \n 2.Login your Account \n 3.Exit")

    user_input=int(input("Enter your choise"))

    if user_input == 3:
        break
    elif user_input == 1:
        b.create_Account()
    elif user_input == 2:
        name=input("Enter your name:")
        password=input("Enter your password:")

        flag=0
        isAdmin=False

        if name == "Waqas" and password=="waqas12":
            isAdmin=True
        if isAdmin==False:
            for user in b.get_users():
                if user['username']==name and user['password']==password:
                    flag=1
                    break
            if flag:
                while True:
                    print(f"\n{''*10}Wellcome to waqas bus ticket booking system")
                    print("1. Available Buses: \n2. Show bus Info:\n3.Reservation\n4.Exit")
                    a=int(input("Enter your choies :"))
                    if a == 4:
                        break
                    elif a == 1:
                        b.Avilable_buses()
                    elif a == 2:
                        b.show_ticket()
                    elif a == 3:
                        b.reservstion()
            else:
                print("No user found")
        else:
            while True:
                print(f"\n {' '*10} Hello Admin WELLCOME to waqas Bus ticket booking system")
                print("1. Add Bus\n2.Available Buses\n3.Show bus Info\n4.Exit") 
                a=int(input("Enter your choice:"))
                if a==4:
                    break
                elif a==1:
                    b.add_bus()
                elif a==2:
                    b.Avilable_buses()   
                elif a==3:
                    b.show_ticket()


c=Counter()
c.reservstion()



    
