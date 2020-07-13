import unittest
import image_manager
from unittest import mock


class TestImageManager(unittest.TestCase):
	def setUp(self):
		self.image_manager = image_manager.ImageManager()

	@mock.patch('pygame.transform.scale')
	@mock.patch('pygame.image.load')
	def testPut(self, mock_image_load, mock_transform_scale):
		image_filepath = 'MOCK_FILEPATH'
		image_id = 'MOCK_ID'
		size = (10, 10)
		
		image = mock.Mock()
		mock_image_load.return_value = image
		resized_image = mock.Mock()
		mock_transform_scale.return_value = resized_image

		self.image_manager.put(image_id, image_filepath, size)

		self.assertEqual(resized_image, self.image_manager.images.get(image_id))
		mock_image_load.assert_called_once_with(image_filepath)
		mock_transform_scale.assert_called_once_with(image, size)

	def testGet(self):
		image_id = 'MOCK_ID'
		image = mock.Mock()
		self.image_manager.images[image_id] = image

		result = self.image_manager.get(image_id)

		self.assertEqual(result, image)


if __name__ == '__main__':
	unittest.main()