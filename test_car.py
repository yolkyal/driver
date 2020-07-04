import unittest
from math import radians, sin, cos, pi, atan
import car


class TestCar(unittest.TestCase):
	def setUp(self):
		self.pos = (100, 100)
		self.car_length = 50
		self.car_angle = pi / 2
		self.wheel_angle = pi / 2
		self.car = car.Car(self.pos, self.car_length, self.car_angle, self.wheel_angle)

	def testGetFrontPos(self):
		car_front_pos_x = self.pos[0] + self.car_length * 0.5 * cos(self.car_angle)
		car_front_pos_y = self.pos[1] + self.car_length * 0.5 * sin(self.car_angle)

		car_front_pos = self.car.get_front_pos()

		self.assertEqual(car_front_pos_x, car_front_pos[0])
		self.assertEqual(car_front_pos_y, car_front_pos[1])
		
	def testGetBackPos(self):
		car_back_pos_x = self.pos[0] - self.car_length * 0.5 * cos(self.car_angle)
		car_back_pos_y = self.pos[1] - self.car_length * 0.5 * sin(self.car_angle)

		car_back_pos = self.car.get_back_pos()

		self.assertEqual(car_back_pos_x, car_back_pos[0])
		self.assertEqual(car_back_pos_y, car_back_pos[1])

	def testMove(self):
		mov = 1

		# current front and back positions
		car_front_pos_x = self.pos[0] + self.car_length * 0.5 * cos(self.car_angle)
		car_front_pos_y = self.pos[1] + self.car_length * 0.5 * sin(self.car_angle)
		car_back_pos_x = self.pos[0] - self.car_length * 0.5 * cos(self.car_angle)
		car_back_pos_y = self.pos[1] - self.car_length * 0.5 * sin(self.car_angle)

		# move front position in direction of front wheels
		car_front_pos_x += mov * cos(self.wheel_angle)
		car_front_pos_y += mov * sin(self.wheel_angle)

		# move back position in direction of car
		car_back_pos_x  += mov * cos(self.car_angle)
		car_back_pos_y += mov * sin(self.car_angle)

		# calculate new centre using new front and back positions
		new_centre = ((car_front_pos_x - car_back_pos_x) / 2, (car_front_pos_y - car_back_pos_y) / 2)

		# calculate new car angle using front and back positions
		new_car_angle = atan((car_front_pos_x - car_back_pos_x) / (car_front_pos_y - car_back_pos_y))

		self.car.move(mov)

		self.assertEqual(new_centre, self.car.pos)
		self.assertEqual(new_car_angle, self.car.car_angle)


if __name__ == '__main__':
	unittest.main()

