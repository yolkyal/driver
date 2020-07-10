import pygame

class CarController:
	def __init__(self, car):
		self.car = car
		self.is_accelerating = False
		self.is_reversing = False

	def handle_event(self, e):
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_UP:
				self.is_accelerating = True
			elif e.key == pygame.K_DOWN:
				self.is_reversing = True
			elif e.key == pygame.K_LEFT:
				self.car.steer_left()
			elif e.key == pygame.K_RIGHT:
				self.car.steer_right()
		elif e.type == pygame.KEYUP:
			if e.key == pygame.K_UP:
				self.is_accelerating = False
			elif e.key == pygame.K_DOWN:
				self.is_reversing = False

	def update(self):
		if self.is_accelerating:
			self.car.accelerate()
		if self.is_reversing:
			self.car.reverse()