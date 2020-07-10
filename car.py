import math
import trig_utils


DEFAULT_ACCELERATION = 0.3
DEFAULT_STEER = math.pi / 128
DEFAULT_SPEED_DAMPING = 0.97
SPEED_EPSILON = 0.01
DEFAULT_STEER_LIMIT = math.pi / 4


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
			new_back_pos = trig_utils.calc_point(self.get_back_pos(), self.car_angle, math.cos(self.wheel_angle - self.car_angle) * self.speed)

			self.pos = ((new_front_pos[0] + new_back_pos[0]) / 2, (new_front_pos[1] + new_back_pos[1]) / 2)

			x_diff = new_front_pos[0] - new_back_pos[0]
			y_diff = new_front_pos[1] - new_back_pos[1]

			new_car_angle = math.atan2(new_front_pos[1] - new_back_pos[1], new_front_pos[0] - new_back_pos[0])
			self.wheel_angle += new_car_angle - self.car_angle
			self.car_angle = new_car_angle

	def accelerate(self):
		self.speed += DEFAULT_ACCELERATION

	def reverse(self):
		self.speed -= DEFAULT_ACCELERATION

	def steer_right(self):
		self.wheel_angle += DEFAULT_STEER
		if self.wheel_angle - self.car_angle > DEFAULT_STEER_LIMIT:
			self.wheel_angle = self.car_angle + DEFAULT_STEER_LIMIT

	def steer_left(self):
		self.wheel_angle -= DEFAULT_STEER
		if self.wheel_angle - self.car_angle < -DEFAULT_STEER_LIMIT:
			self.wheel_angle = self.car_angle - DEFAULT_STEER_LIMIT

	def get_front_pos(self):
		return trig_utils.calc_point(self.pos, self.car_angle, self.half_car_length)

	def get_back_pos(self):
		return trig_utils.calc_point(self.pos, self.car_angle, -self.half_car_length)

	def get_front_wheels(self):
		return trig_utils.calc_mid_point(self.get_front_pos(), self.car_angle + math.pi / 2, self.car_width)

	def get_back_wheels(self):
		return trig_utils.calc_mid_point(self.get_back_pos(), self.car_angle + math.pi / 2, self.car_width)