import unittest
import math
import car
from unittest import mock


class TestCar(unittest.TestCase):
	def setUp(self):
		self.pos = (100, 100)
		self.car_length = 50
		self.car_width = 30
		self.car_angle = math.pi / 4
		self.wheel_angle = math.pi / 4
		self.car = car.Car(self.pos, self.car_length, self.car_width, self.car_angle, self.wheel_angle)

	def testAccelerate(self):
		self.car.accelerate()
		
		self.assertEqual(self.car.speed, car.DEFAULT_ACCELERATION)

	def testReverse(self):
		self.car.reverse()

		self.assertEqual(self.car.speed, -car.DEFAULT_ACCELERATION)

	def testSteerLeft(self):
		self.car.steer_left()

		self.assertEqual(self.car.wheel_angle, math.pi / 4 - car.DEFAULT_STEER)

	def testSteerRight(self):
		self.car.steer_right()

		self.assertEqual(self.car.wheel_angle, math.pi / 4 + car.DEFAULT_STEER)

	def testSpeedDamping(self):
		self.car.speed = 1

		self.car.update()

		self.assertEqual(self.car.speed, 1 * car.DEFAULT_SPEED_DAMPING)

	def testSpeedEpsilon(self):
		self.car.speed = car.SPEED_EPSILON

		self.car.update()

		self.assertEqual(0, self.car.speed)

	def testGetTrueWheelAngle(self):
		self.assertEqual(self.car.car_angle + self.car.wheel_angle, self.car.get_true_wheel_angle())

	@mock.patch('trig_utils.calc_point')
	def testGetFrontPos(self, mock_calc_point):
		car_front_pos = mock.Mock()
		mock_calc_point.return_value = car_front_pos

		result = self.car.get_front_pos()

		self.assertEqual(result, car_front_pos)
		mock_calc_point.assert_called_once_with(self.pos, self.car_angle, self.car_length / 2)
		
	@mock.patch('trig_utils.calc_point')
	def testGetBackPos(self, mock_calc_point):
		car_back_pos = mock.Mock()
		mock_calc_point.return_value = car_back_pos

		result = self.car.get_back_pos()

		self.assertEqual(result, car_back_pos)
		mock_calc_point.assert_called_once_with(self.pos, self.car_angle, -self.car_length / 2)

	@mock.patch('trig_utils.calc_mid_point')
	@mock.patch('trig_utils.calc_point')
	def testGetFrontWheels(self, mock_calc_point, mock_calc_mid_point):
		car_front_pos = mock.Mock()
		wheel_front_right = mock.Mock()
		wheel_front_left = mock.Mock()
		mock_calc_point.return_value = car_front_pos
		mock_calc_mid_point.return_value = (wheel_front_right, wheel_front_left)

		result = self.car.get_front_wheels()

		self.assertEqual(result, (wheel_front_right, wheel_front_left))
		mock_calc_point.assert_called_once_with(self.pos, self.car_angle, self.car_length / 2)
		mock_calc_mid_point.assert_called_once_with(car_front_pos, self.car_angle + math.pi / 2, self.car_width)
	
	@mock.patch('trig_utils.calc_mid_point')
	@mock.patch('trig_utils.calc_point')
	def testGetBackWheels(self, mock_calc_point, mock_calc_mid_point):
		car_back_pos = mock.Mock()
		wheel_back_right = mock.Mock()
		wheel_back_left = mock.Mock()
		mock_calc_point.return_value = car_back_pos
		mock_calc_mid_point.return_value = (wheel_back_right, wheel_back_left)

		result = self.car.get_back_wheels()

		self.assertEqual(result, (wheel_back_right, wheel_back_left))
		mock_calc_point.assert_called_once_with(self.pos, self.car_angle, -self.car_length / 2)
		mock_calc_mid_point.assert_called_once_with(car_back_pos, self.car_angle + math.pi / 2, self.car_width)

	def testUpdate(self):
		speed = 1
		self.car.speed = speed
		speed *= car.DEFAULT_SPEED_DAMPING

		# current front and back positions
		car_front_pos_x = self.pos[0] + self.car_length * 0.5 * math.cos(self.car_angle)
		car_front_pos_y = self.pos[1] + self.car_length * 0.5 * math.sin(self.car_angle)
		car_back_pos_x = self.pos[0] - self.car_length * 0.5 * math.cos(self.car_angle)
		car_back_pos_y = self.pos[1] - self.car_length * 0.5 * math.sin(self.car_angle)

		# move front position in direction of front wheels
		true_wheel_angle = self.car.car_angle + self.car.wheel_angle

		car_front_pos_x += speed * math.cos(true_wheel_angle)
		car_front_pos_y += speed * math.sin(true_wheel_angle)

		# move back position in direction of car
		car_back_pos_x  += speed * math.cos(self.car_angle)
		car_back_pos_y += speed * math.sin(self.car_angle)

		# calculate new centre using new front and back positions
		new_centre = ((car_front_pos_x + car_back_pos_x) / 2, (car_front_pos_y + car_back_pos_y) / 2)

		# calculate new car angle using front and back positions
		new_car_angle = math.atan2(car_front_pos_y - car_back_pos_y, car_front_pos_x - car_back_pos_x)

		self.car.update()

		self.assertEqual(new_centre, self.car.pos)
		self.assertEqual(new_car_angle, self.car.car_angle)


if __name__ == '__main__':
	unittest.main()

