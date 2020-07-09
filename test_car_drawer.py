import unittest
import math
import car_drawer, trig_utils
from unittest import mock


class TestCarDrawer(unittest.TestCase):
	def setUp(self):
		self.d_surf = mock.Mock()

		self.front_pos = (100, 100)
		self.back_pos = (200, 200)

		self.car = mock.Mock()
		self.car.get_front_pos.return_value = self.front_pos
		self.car.get_back_pos.return_value = self.back_pos
		self.car.car_angle = math.pi / 4
		self.car.wheel_angle = math.pi / 4

		self.wheel_length = 10
		self.car_drawer = car_drawer.CarDrawer(self.wheel_length)

	@mock.patch('pygame.draw.line')
	@mock.patch('pygame.draw.lines')
	def testDraw(self, mock_draw_lines, mock_draw_line):
		front_wheel_left = (100, 101)
		front_wheel_right = (102, 103)
		front_wheel_positions = (front_wheel_left, front_wheel_right)

		back_wheel_left = (200, 201)
		back_wheel_right = (202, 203)
		back_wheel_positions = (back_wheel_left, back_wheel_right)

		self.car.get_front_wheels.return_value = front_wheel_positions
		self.car.get_back_wheels.return_value = back_wheel_positions

		self.car_drawer.draw(self.d_surf, self.car)

		mock_draw_lines.assert_called_once_with(self.d_surf, car_drawer.DEFAULT_CHASSIS_COLOUR, True, [front_wheel_left, front_wheel_right, back_wheel_right, back_wheel_left])

		front_wheel_left_pts = trig_utils.calc_mid_point(front_wheel_left, self.car.wheel_angle, self.wheel_length)
		front_wheel_right_pts = trig_utils.calc_mid_point(front_wheel_right, self.car.wheel_angle, self.wheel_length)
		back_wheel_left_pts = trig_utils.calc_mid_point(back_wheel_left, self.car.car_angle, self.wheel_length)
		back_wheel_right_pts = trig_utils.calc_mid_point(back_wheel_right, self.car.car_angle, self.wheel_length)

		expected_line_calls = [
		mock.call(self.d_surf, car_drawer.DEFAULT_WHEEL_COLOUR, front_wheel_left_pts[0], front_wheel_left_pts[1]),
		mock.call(self.d_surf, car_drawer.DEFAULT_WHEEL_COLOUR, front_wheel_right_pts[0], front_wheel_right_pts[1]),
		mock.call(self.d_surf, car_drawer.DEFAULT_WHEEL_COLOUR, back_wheel_left_pts[0], back_wheel_left_pts[1]),
		mock.call(self.d_surf, car_drawer.DEFAULT_WHEEL_COLOUR, back_wheel_right_pts[0], back_wheel_right_pts[1])
		]

		self.assertEqual(expected_line_calls, mock_draw_line.call_args_list)


if __name__ == '__main__':
	unittest.main()