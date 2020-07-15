import unittest
import math
import car_drawer, trig_utils
from unittest import mock


class TestCarDrawer(unittest.TestCase):
	def setUp(self):
		self.d_surf = mock.Mock()
		
		self.car = mock.Mock()
		self.car.id = 'CAR_1'
		self.car.pos = (100, 100)
		self.car.car_angle = math.pi / 4
		self.car.wheel_angle = math.pi / 4

		self.image_manager = mock.Mock()

		self.car_drawer = car_drawer.CarDrawer(self.image_manager)

	@mock.patch('pygame.transform.rotate')
	def testDrawChassis(self, mock_transform_rotate):
		car_img_surf = mock.Mock()
		self.image_manager.get.return_value = car_img_surf
		mock_rot_img_srf = mock.Mock()
		mock_rot_img_srf.get_width.return_value = 50
		mock_rot_img_srf.get_height.return_value = 30
		mock_transform_rotate.return_value = mock_rot_img_srf

		self.car_drawer.drawChassis(self.d_surf, self.car)

		self.image_manager.get.assert_called_once_with(self.car.id)
		mock_transform_rotate.assert_called_once_with(car_img_surf, math.degrees(1.5 * math.pi - self.car.car_angle))
		self.d_surf.blit.assert_called_once_with(mock_rot_img_srf, (self.car.pos[0] - 25, self.car.pos[1] - 15))

	@mock.patch('pygame.transform.rotate')
	def testDrawWheels(self, mock_transform_rotate):
		wheel_img_surf = mock.Mock()
		self.image_manager.get.return_value = wheel_img_surf

		front_wheel_positions = ((100, 100), (200, 200))
		self.car.get_front_wheels.return_value = front_wheel_positions

		mock_rot_img_srf = mock.Mock()
		mock_rot_img_srf.get_width.return_value = 2
		mock_rot_img_srf.get_height.return_value = 10
		mock_transform_rotate.return_value = mock_rot_img_srf

		self.car_drawer.drawWheels(self.d_surf, self.car)

		self.image_manager.get.assert_called_once_with(self.car.wheel_id)
		mock_transform_rotate.assert_called_once_with(wheel_img_surf, math.degrees(1.5 * math.pi - self.car.wheel_angle))

		expected_blit_calls = [mock.call(mock_rot_img_srf, (front_wheel_positions[0][0] - 1, front_wheel_positions[0][1] - 5)), 
		mock.call(mock_rot_img_srf, (front_wheel_positions[1][0] - 1, front_wheel_positions[1][1] - 5))]
		self.assertEqual(expected_blit_calls, self.d_surf.blit.call_args_list)

if __name__ == '__main__':
	unittest.main()