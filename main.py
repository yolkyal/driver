import sys
import pygame
import math

from car import Car
from car_controller import CarController
from car_drawer import CarDrawer


BG_COL = (220, 220, 220)


def main():
	pygame.init()
	size = width, height = 400, 400
	d_surf = pygame.display.set_mode(size)
	clock = pygame.time.Clock()

	car_start_pos = (200, 200)
	car_length = 50
	car_width = 20
	car_angle = math.pi / 2
	wheel_angle = math.pi / 2

	car = Car(car_start_pos, car_length, car_width, car_angle, wheel_angle)
	car_controller = CarController(car)
	car_drawer = CarDrawer(10)

	while True:
		delta_ms = clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type in (pygame.KEYUP, pygame.KEYDOWN):
				car_controller.handle_event(event)
				
		car_controller.update()
		car.update()

		d_surf.fill(BG_COL)
		car_drawer.draw(d_surf, car)
		pygame.display.update()
	

if __name__ == '__main__':
	main()
