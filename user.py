class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password

    
class Bus:
    def __init__(self,coach,driver,arrival,departure,from_des,to):
        self.coach=coach
        self.driver=driver
        self.arrival=arrival
        self.from_des=from_des
        self.to=to
        self.departure=departure
        self.seat=["Empty"for i in range(20)]
# b=Bus(2,"waqas","12 am","12pm","karachi","mardan")     for checking class its work or not
# print(vars(b))

class waqas:
    total_bus=3
    total_bus_list=[]

    def add_bus(self):
        bus_no=int(input("Enter bus no"))
        flag=1
        for bus in self.total_bus_list:
            if bus_no==bus["coach"]:
                print("Bus is already Added:")
                flag=0
                break
        if flag:
            bus_driver=input("Enter bus driver name:")
            bus_arrival=input("Enter bus arrival time ")
            bus_departure=input("Enter bus departure time:")
            bus_from=input("Enter bus starting point:")
            bus_to=input("Enter bus ending point:")
            self.new_bus=Bus(bus_no,bus_driver,bus_arrival,bus_departure,bus_from,bus_to)
            self.total_bus_list.append(vars(self.new_bus))
            print("Bus Added sucessfully:")

company=waqas()
company.add_bus()
