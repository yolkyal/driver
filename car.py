import math
import trig_utils


DEFAULT_ACCELERATION = 0.1
DEFAULT_STEER = math.pi / 32
DEFAULT_SPEED_DAMPING = 0.99
SPEED_EPSILON = 0.01


class Car:
	def __init__(self, pos, car_length, car_width, car_angle=0, wheel_angle=0):
		self.pos = pos
		self.car_length = car_length
		self.car_width = car_width
		self.car_angle = car_angle
		self.wheel_angle = wheel_angle
		self.half_car_length = car_length / 2
		self.half_car_width = car_width / 2
		self.speed = 0

	def update(self):
		self.speed *= DEFAULT_SPEED_DAMPING
		if abs(self.speed) <= SPEED_EPSILON:
			self.speed = 0
		else:
			new_front_pos = trig_utils.calc_point(self.get_front_pos(), self.wheel_angle, self.speed)
			new_back_pos = trig_utils.calc_point(self.get_back_pos(), self.car_angle, self.speed)

			x_diff = new_front_pos[0] - new_back_pos[0]
			y_diff = new_front_pos[1] - new_back_pos[1]

			self.pos = (x_diff / 2, y_diff / 2)

			# zero division safety
			if x_diff == 0:
				self.car_angle = math.pi / 2 if y_diff > 0 else (3 * math.pi) / 2
			else:
				self.car_angle = math.atan((new_front_pos[1] - new_back_pos[1]) / (new_front_pos[0] - new_back_pos[0]))

	def accelerate(self):
		self.speed += DEFAULT_ACCELERATION

	def reverse(self):
		self.speed -= DEFAULT_ACCELERATION

	def steer_right(self):
		self.wheel_angle += DEFAULT_STEER

	def steer_left(self):
		self.wheel_angle -= DEFAULT_STEER

	def get_front_pos(self):
		return trig_utils.calc_point(self.pos, self.car_angle, self.half_car_length)

	def get_back_pos(self):
		return trig_utils.calc_point(self.pos, self.car_angle, -self.half_car_length)

	def get_front_wheels(self):
		return trig_utils.calc_mid_point(self.get_front_pos(), self.car_angle, self.car_width)

	def get_back_wheels(self):
		return trig_utils.calc_mid_point(self.get_back_pos(), self.car_angle, self.car_width)