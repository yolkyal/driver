import pygame
import trig_utils


DEFAULT_CHASSIS_COLOUR = (50, 50, 50)
DEFAULT_WHEEL_COLOUR = (200, 0, 0)


class CarDrawer:
	def __init__(self, wheel_length):
		self.wheel_length = wheel_length

	def draw(self, d_surf, car):
		front_wheels = car.get_front_wheels()
		back_wheels = car.get_back_wheels()

		front_wheel_left_pts = trig_utils.calc_mid_point(front_wheels[0], car.wheel_angle, self.wheel_length)
		front_wheel_right_pts = trig_utils.calc_mid_point(front_wheels[1], car.wheel_angle, self.wheel_length)
		back_wheel_left_pts = trig_utils.calc_mid_point(back_wheels[0], car.car_angle, self.wheel_length)
		back_wheel_right_pts = trig_utils.calc_mid_point(back_wheels[1], car.car_angle, self.wheel_length)

		pygame.draw.lines(d_surf, DEFAULT_CHASSIS_COLOUR, True, [front_wheels[0], front_wheels[1], back_wheels[1], back_wheels[0]])

		pygame.draw.line(d_surf, DEFAULT_WHEEL_COLOUR, front_wheel_left_pts[0], front_wheel_left_pts[1])
		pygame.draw.line(d_surf, DEFAULT_WHEEL_COLOUR, front_wheel_right_pts[0], front_wheel_right_pts[1])
		pygame.draw.line(d_surf, DEFAULT_WHEEL_COLOUR, back_wheel_left_pts[0], back_wheel_left_pts[1])
		pygame.draw.line(d_surf, DEFAULT_WHEEL_COLOUR, back_wheel_right_pts[0], back_wheel_right_pts[1])