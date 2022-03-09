from vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self,starting_top_speed=200):
        super().__init__(starting_top_speed)
        self.__passengers=[]
    def get_passengers(self):
        return self.__passengers
    def add_group(self,passengers):
        self.__passengers.extend(passengers)

bus1=Bus()
bus1.drive()
bus1.add_group([1,2,4])
print(bus1.get_passengers())
