class Vehicle:
    	# top_speed=100
	# warnings = []
	def __init__(self,starting_top_speed = 100):
		self.__top_speed = starting_top_speed
		self.__warnings = []

	def add_warning(self,element):
			self.__warnings.append(element)
	def add_warnings(self,elements):
			self.__warnings.extend(elements)
	def __repr__(self):
		print('Printing...')
		return 'Top Speed: {} , Warnings: {}'.format(self.__top_speed,str(self.__warnings))
		
	def drive(self):
		print('I am driving but certainly not faster than {}'.format(self.__top_speed))