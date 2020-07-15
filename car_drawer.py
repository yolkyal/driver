import pygame
import math
import trig_utils


DEFAULT_CHASSIS_COLOUR = (50, 50, 50)
DEFAULT_WHEEL_COLOUR = (200, 0, 0)


class CarDrawer:
	def __init__(self, image_manager):
		self.image_manager = image_manager

	def draw(self, d_surf, car):
		self.drawWheels(d_surf, car)
		self.drawChassis(d_surf, car)

	def drawChassis(self, d_surf, car):
		rot_car_img_srf = pygame.transform.rotate(self.image_manager.get(car.id), math.degrees(1.5 * math.pi - car.car_angle))
		image_pos = (car.pos[0] - rot_car_img_srf.get_width() / 2, car.pos[1] - rot_car_img_srf.get_height() / 2)
		d_surf.blit(rot_car_img_srf, image_pos)

	def drawWheels(self, d_surf, car):
		rot_wheel_img_srf = pygame.transform.rotate(self.image_manager.get(car.wheel_id), math.degrees(1.5 * math.pi - car.wheel_angle))
		front_wheels = car.get_front_wheels()
		left_wheel_pos = (front_wheels[0][0] - rot_wheel_img_srf.get_width() / 2, front_wheels[0][1] - rot_wheel_img_srf.get_height() / 2)
		right_wheel_pos = (front_wheels[1][0] - rot_wheel_img_srf.get_width() / 2, front_wheels[1][1] - rot_wheel_img_srf.get_height() / 2)
		d_surf.blit(rot_wheel_img_srf, left_wheel_pos)
		d_surf.blit(rot_wheel_img_srf, right_wheel_pos)