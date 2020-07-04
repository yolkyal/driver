import math

class Car:
	def __init__(self, pos, car_length, car_angle=0, wheel_angle=0):
		self.pos = pos
		self.car_length = car_length
		self.car_angle = car_angle
		self.wheel_angle = wheel_angle
		self.half_car_length = car_length / 2

	def get_front_pos(self):
		front_pos_x = self.pos[0] + self.half_car_length * math.cos(self.car_angle)
		front_pos_y = self.pos[1] + self.half_car_length * math.sin(self.car_angle)
		return (front_pos_x, front_pos_y)

	def get_back_pos(self):
		back_pos_x = self.pos[0] - self.half_car_length * math.cos(self.car_angle)
		back_pos_y = self.pos[1] - self.half_car_length * math.sin(self.car_angle)
		return (back_pos_x, back_pos_y)

	def move(self, mov):
		new_front_pos = self._get_front_with_move(mov)
		new_back_pos = self._get_back_with_move(mov)

		x_diff = new_front_pos[0] - new_back_pos[0]
		y_diff = new_front_pos[1] - new_back_pos[1]

		self.pos = (x_diff / 2, y_diff / 2)

		# zero division safety
		if x_diff == 0:
			self.car_angle = math.pi / 2 if y_diff > 0 else (3 * math.pi) / 2
		else:
			self.car_angle = math.atan((new_front_pos[1] - new_back_pos[1]) / (new_front_pos[0] - new_back_pos[0]))

	def _get_front_with_move(self, mov):
		front_pos = self.get_front_pos()
		new_front_pos_x = front_pos[0] + mov * math.cos(self.wheel_angle)
		new_front_pos_y = front_pos[1] + mov * math.sin(self.wheel_angle)
		return (new_front_pos_x, new_front_pos_y)

	def _get_back_with_move(self, mov):
		back_pos = self.get_back_pos()
		new_back_pos_x = back_pos[0] + mov * math.cos(self.car_angle)
		new_back_pos_y = back_pos[1] + mov * math.sin(self.car_angle)
		return (new_back_pos_x, new_back_pos_y)