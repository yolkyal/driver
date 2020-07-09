import unittest
import pygame
import car_controller
from unittest import mock

class TestCarController(unittest.TestCase):
	def setUp(self):
		self.car = mock.Mock()
		self.car_controller = car_controller.CarController(self.car)

	def testSteerLeft(self):
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
		self.car_controller.handle_event(e)
		self.car.steer_left.assert_called_once()

	def testSteerRight(self):
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)
		self.car_controller.handle_event(e)
		self.car.steer_right.assert_called_once()

	def testAccelerate(self):
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
		self.car_controller.handle_event(e)

		self.car_controller.update()

		self.assertTrue(self.car_controller.is_accelerating)
		self.car.accelerate.assert_called_once()

	def testReverse(self):
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)
		self.car_controller.handle_event(e)
		
		self.car_controller.update()

		self.assertTrue(self.car_controller.is_reversing)
		self.car.reverse.assert_called_once()


if __name__ == '__main__':
	unittest.main()