class Car:
	def __init__(self, pos, car_length, car_angle=0, wheel_angle=0):
		self.pos = pos
		self.car_length = car_length
		self.car_angle = car_angle
		self.wheel_angle = wheel_angle

	def get_front_pos(self):
		pass

	def get_back_pos(self):
		pass

	def move(self, mov):
		pass