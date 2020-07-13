import pygame


class ImageManager:
	def __init__(self):
		self.images = {}

	def put(self, k, image_filepath, size):
		image = pygame.image.load(image_filepath)
		image = pygame.transform.scale(image, size)
		self.images[k] = image

	def get(self, image_id):
		return self.images.get(image_id)