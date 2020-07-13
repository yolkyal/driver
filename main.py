import sys
import pygame
import math

from car import Car
from car_controller import CarController
from car_drawer import CarDrawer
from image_manager import ImageManager


BG_COL = (220, 220, 220)


def main():
	pygame.init()
	size = width, height = 800, 800
	d_surf = pygame.display.set_mode(size)
	clock = pygame.time.Clock()

	car_id = 'CAR_ID'
	car_start_pos = (400, 600)
	car_length = 112
	car_width = 64
	car_angle = 0
	wheel_angle = 0

	image_manager = ImageManager()
	image_manager.put(car_id, 'images/car.png', (64, 112))

	car = Car(car_id, car_start_pos, car_length, car_width, car_angle, wheel_angle)
	car_controller = CarController(car)
	car_drawer = CarDrawer(image_manager)

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
