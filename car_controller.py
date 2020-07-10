import pygame

class CarController:
	def __init__(self, car):
		self.car = car
		self.is_accelerating = False
		self.is_reversing = False
		self.is_steering_left = False
		self.is_steering_right = False

	def handle_event(self, e):
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_UP:
				self.is_accelerating = True
			elif e.key == pygame.K_DOWN:
				self.is_reversing = True
			elif e.key == pygame.K_LEFT:
				self.is_steering_left = True
			elif e.key == pygame.K_RIGHT:
				self.is_steering_right = True
		elif e.type == pygame.KEYUP:
			if e.key == pygame.K_UP:
				self.is_accelerating = False
			elif e.key == pygame.K_DOWN:
				self.is_reversing = False
			elif e.key == pygame.K_LEFT:
				self.is_steering_left = False
			elif e.key == pygame.K_RIGHT:
				self.is_steering_right = False

	def update(self):
		if self.is_accelerating:
			self.car.accelerate()
		if self.is_reversing:
			self.car.reverse()
		if self.is_steering_left:
			self.car.steer_left()
		if self.is_steering_right:
			self.car.steer_right()