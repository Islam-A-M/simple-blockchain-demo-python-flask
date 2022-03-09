from vehicle import Vehicle
class Car(Vehicle):
	def __init__(self, starting_top_speed=2000):
		super().__init__(starting_top_speed=starting_top_speed)
	def brag(self):
		print('Look how cool my car is!')

car1 = Car(12)
car1.drive()
car1.add_warning('d')
car1.add_warnings(['d',2])

print(car1)

car2 = Car()
car2.drive()
print(car2)
